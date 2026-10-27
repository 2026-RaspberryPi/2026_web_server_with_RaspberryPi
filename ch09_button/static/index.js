const chart = new Chart(document.getElementById("chart"), {
    type: "line",
    data: {
        labels: [],
        datasets: [{ label: "반응 시간(ms)", data: [] }]
    }
});

const result = document.getElementById("result");
const startBtn = document.getElementById("start");
const stopBtn = document.getElementById("stop");

let round = 0;          // 지금 몇 회째
let count = 0;          // 기록이 나온 횟수 (시간 초과 제외)
let sum = 0;            // 기록의 합
let stopped = false;    // 종료를 눌렀는지

async function play() {
    if (stopped) {             // 종료를 눌렀으면 평균 보여주고 끝
        finish();
        return;
    }

    round = round + 1;
    const response = await fetch("/api/start", { method: "POST" });
    const data = await response.json();
    if (response.ok) {
        count = count + 1;
        sum = sum + data.ms;
        result.textContent = round + "회 : " + data.ms + "ms";
        chart.data.labels.push(round + "회");          // 그래프에 점 추가
        chart.data.datasets[0].data.push(data.ms);
        chart.update();
    } else {
        result.textContent = round + "회 : " + data.message;
    }

    setTimeout(play, 1000);    // 1초 뒤 다음 회
}

function finish() {
    if (count === 0) {
        result.textContent = "기록이 없음";
    } else {
        result.textContent = count + "회 평균 " + Math.round(sum / count) + "ms";
    }
    startBtn.disabled = false;
}

startBtn.addEventListener("click", function () {
    startBtn.disabled = true;
    stopBtn.disabled = false;
    round = 0;
    count = 0;
    sum = 0;
    stopped = false;
    result.textContent = "LED가 켜지면 누르세요!";
    chart.data.labels = [];                 // 그래프 비우기
    chart.data.datasets[0].data = [];
    chart.update();
    play();
});

stopBtn.addEventListener("click", function () {
    stopped = true;
    stopBtn.disabled = true;
});

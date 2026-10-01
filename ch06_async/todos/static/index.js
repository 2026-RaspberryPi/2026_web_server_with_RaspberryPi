const todos = document.querySelector('#todos')

todos.addEventListener('click', function () {
    fetch('https://jsonplaceholder.typicode.com/todos')   // 기본 method는 GET
        .then(function (response) {
            // 404, 500 등은 catch로 가지 않으므로 직접 확인
            if (!response.ok) {
                throw new Error('HTTP 오류: ' + response.status)
            }
            return response.json()   // JSON 문자열 → 자바스크립트 배열
        })
        .then(function (result) {
            console.log(result)
            let tableData = ""
            for (const obj of result) {
                console.log(obj.title)
                tableData += "<tr>"
                tableData += "<td>" + obj.userId + "</td>"
                tableData += "<td>" + obj.title + "</td>"
                tableData += "<td>" + obj.completed + "</td>"
                tableData += "</tr>"
            }
            document.querySelector("#data").innerHTML += tableData
        })
        .catch(function (error) {
            console.log(error)
        })
})

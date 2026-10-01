var setAngle = document.querySelector('#setAngle')

setAngle.addEventListener('click', function(){
    const angle = document.querySelector('#angle').value;
    if(angle >= 0 && angle <= 180) {
        fetch('/api/angle', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ angle: angle })
        })
        .then(function(response) {
            // fetch는 4xx/5xx 응답에도 실패로 처리하지 않으므로 직접 확인
            if (!response.ok) {
                throw new Error('HTTP ' + response.status)
            }
            return response.json()
        })
        .then(function(result) {
            alert(result.message)
        })
        .catch(function(error) {
            console.log(error)
        })
    }
    else {
        alert("please enter an angle between 0 and 180!!!")
    }
});

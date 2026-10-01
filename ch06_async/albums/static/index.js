const moreBtn = document.querySelector('#more')
const gallery = document.querySelector('#gallery')
let page = 2   // 1페이지(처음 5장)는 Flask가 이미 보여주므로 2부터 시작

// async / await 방식으로 작성한 fetch
moreBtn.addEventListener('click', async function () {
    console.log("버튼 클릭")
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/photos?_page=' + page + '&_limit=5')
        // 404, 500 등은 catch로 가지 않으므로 직접 확인
        if (!response.ok) {
            throw new Error('HTTP 오류: ' + response.status)
        }
        const photos = await response.json()   // JSON 문자열 → 자바스크립트 배열
        console.log(photos)

        let galleryHtml = '<div class="card-group">'   // 사진 5장을 한 줄로 묶음
        photos.forEach(photo => {
            galleryHtml += `
            <div class="card" style="width: 18rem;">
                <img src="${photo.url}" class="card-img-top" alt="로딩중">
                <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">${photo.title}</p>
                </div>
            </div>
            `
        })
        galleryHtml += '</div>'

        // innerHTML = … 은 기존 내용을 덮어쓰고, insertAdjacentHTML('beforeend') 는 맨 뒤에 추가
        gallery.insertAdjacentHTML('beforeend', galleryHtml)
        page++   // 다음 클릭 때는 다음 페이지
    } catch (error) {
        console.log(error)
    }
})

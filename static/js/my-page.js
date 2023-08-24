// 개인정보 변경 버튼 클릭 시 동작
document.getElementById("personalInfo").addEventListener("click", function () {
  alert("개인정보 변경 페이지로 이동합니다.");
});

// 비밀번호 변경 버튼 클릭 시 동작
document.getElementById("passwordChange").addEventListener("click", function () {
  alert("비밀번호 변경 페이지로 이동합니다.");
});

// 로그아웃 버튼 클릭 시 동작
document.getElementById("logout").addEventListener("click", function () {
  alert("로그아웃합니다.");
});

// "내가 쓴 글" 박스 클릭 시 하위 항목들 토글 동작
const postButton = document.querySelector(".post-button");
const subItems = document.querySelector(".sub-items");
postButton.addEventListener("click", function () {
  subItems.classList.toggle("show");
});

// 하위 항목 버튼 클릭 시 동작
const subItemButtons = document.querySelectorAll(".sub-item-button");
subItemButtons.forEach((button) => {
  button.addEventListener("click", function () {
    alert(this.textContent);
  });
});

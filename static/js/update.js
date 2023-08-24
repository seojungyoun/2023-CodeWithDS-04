const form = document.getElementById("personal-info-form");

form.addEventListener("submit", function (event) {
  event.preventDefault(); // 폼의 기본 동작(페이지 리로딩) 방지

  const name = form.elements.name.value;
  const birthdate = form.elements.birthdate.value;
  const username = form.elements.username.value;
  const phone = form.elements.phone.value;

  // 여기서 개인정보를 저장하거나 처리하는 로직을 추가할 수 있습니다.
  // 예: 서버에 전송, 브라우저 내부 저장소에 저장 등
  console.log("이름:", name);
  console.log("생년월일:", birthdate);
  console.log("아이디:", username);
  console.log("전화번호:", phone);

  // 저장 완료 메시지 또는 리다이렉션 등 추가 가능
});

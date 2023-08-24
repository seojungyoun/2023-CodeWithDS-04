document.getElementById("passwordChangeForm").addEventListener("submit", function (event) {
  event.preventDefault();

  var username = document.getElementById("username").value;
  var oldPassword = document.getElementById("oldPassword").value;
  var newPassword = document.getElementById("newPassword").value;

  if (newPassword !== confirmNewPassword) {
    document.getElementById("message").innerText = "새로운 비밀번호가 일치하지 않습니다.";
    return;
  }

  document.getElementById("message").innerText = "비밀번호가 성공적으로 변경되었습니다.";
});

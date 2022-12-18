let activeIndex = 0;
// Placeholders
username_input = document.getElementById("id_username");
if (username_input){
  username_input.placeholder = "Логин";
};
password_input = document.getElementById("id_password");
if (password_input){
  password_input.placeholder = "Пароль";
};
old_password_input = document.getElementById("id_old_password");
if (old_password_input){
  old_password_input.placeholder = "Старый пароль";
};
new_password1_input = document.getElementById("id_new_password1");
if (new_password1_input){
  new_password1_input.placeholder = "Новый пароль";
};
new_password2_input = document.getElementById("id_new_password2");
if (new_password2_input){
  new_password2_input.placeholder = "Повторите пароль";
};
email_input = document.getElementById("id_email")
if (email_input){
  email_input.placeholder = "Адрес электронной почты"

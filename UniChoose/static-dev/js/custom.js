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
  email_input.placeholder = "Адресс электронной почты"
}


// cards
const cards = document.getElementsByClassName("card-group");

const handleLikeClick = () => {
    const nextIndex = activeIndex + 1;

    const currentCard = document.querySelector(`[data-index="${activeIndex}"]`),
        nextCard = document.querySelector(`[data-index="${nextIndex}"]`)
    
    
    currentCard.dataset.status = "inactive"

    setTimeout(() => {
    nextCard.dataset.status = "active";
    activeIndex = nextIndex;
  });
}
const handleDislikeClick = () => {
    const nextIndex = activeIndex + 1;

    const currentCard = document.querySelector(`[data-index="${activeIndex}"]`),
        nextCard = document.querySelector(`[data-index="${nextIndex}"]`)
    
    
    currentCard.dataset.status = "inactive"

    setTimeout(() => {
    nextCard.dataset.status = "active";
    activeIndex = nextIndex;
  });
}
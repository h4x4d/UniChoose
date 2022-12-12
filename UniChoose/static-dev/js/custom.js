let activeIndex = 0;

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
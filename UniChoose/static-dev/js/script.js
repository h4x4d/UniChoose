const swiper = document.querySelector('#swiper');

// constants
const urls = [
    'https://source.unsplash.com/random/1000x1000/?sky',
    'https://source.unsplash.com/random/1000x1000/?landscape',
];

// variables
let cardCount = 0;

// functions
function appendNewCard() {
    const request = new Request('/api/preference/');
    fetch(request).then(response => {
        response.json().then(r => {
            const card = new Card({
                department: r['results'][0],
                onDismiss: appendNewCard,
                onLike: like_func,
                onDislike: dislike_func
            });
            swiper.append(card.element);

        })

    })

    cardCount++;
    console.log(cardCount)

    const cards = swiper.querySelectorAll('.card:not(.dismissing)');
    cards.forEach((card, index) => {
        card.style.setProperty('--i', index);
    });
}

// first 5 cards
for (let i = 0; i < 1; i++) {
    appendNewCard();
}

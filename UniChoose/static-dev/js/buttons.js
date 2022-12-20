like_func = function (id) {
    like.style.animationPlayState = 'running';
    like.classList.toggle('trigger');

    const request = new Request('/api/like/' + id + '/');

    return fetch(request)

};
dislike_func = function (id) {
    dislike.style.animationPlayState = 'running';
    dislike.classList.toggle('trigger');

    const request = new Request('/api/dislike/' + id + '/');

    return fetch(request)

};
like_button = function () {
    window.card.startPoint = {x: 100, y: 100}
    window.card.handleMove(10000, 100)
}
dislike_button = function () {
    window.card.startPoint = {x: 1000, y: 100}
    window.card.handleMove(0, 100)
}
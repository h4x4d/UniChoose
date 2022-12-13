like_func = function (id) {
  like.style.animationPlayState = 'running';
  like.classList.toggle('trigger');

  const request = new Request('/api/like/' + id + '/');

  fetch(request)

};
dislike_func = function (id) {
  like.style.animationPlayState = 'running';
  like.classList.toggle('trigger');

  const request = new Request('/api/dislike/' + id + '/');

  fetch(request)

};
document.addEventListener('DOMContentLoaded', function () {
  // Ваш код здесь

  var btn = document.getElementById('btn');
  var btn1 = document.getElementById('ab')

  btn.addEventListener('click', function () {
    console.log('xui')
    btn1.classList.toggle('active')
  });
});


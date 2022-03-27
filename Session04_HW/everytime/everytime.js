var navSwiper = null;

var navSwiper = new Swiper(".navSwiper", {
  slidesPerView: 'auto',
  freeMode: true,
  
});

var swiper = new Swiper(".mySwiper", {
});



window.addEventListener('resize', () => {
  // navSwiper = null;
  // swiper = null;
  if (navSwiper == null || swiper == null) {

    navSwiper = new Swiper(".navSwiper", {
      slidesPerView: 'auto',
      freeMode: true,
    
    });

    swiper = new Swiper(".mySwiper", {
    });
  }
});



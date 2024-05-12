window.onload = ()=>{

    const hamburger= document.querySelector(".hamburger");
    const menu= document.querySelector(".nav_menu");
    
    hamburger.addEventListener("click", () => {
      hamburger.classList.toggle("active");
      menu.classList.toggle("active");
    })
    
    document.querySelectorAll(".navitem").forEach(n => n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    menu.classList.remove("active");
    
    }))
    
    const swiper = new Swiper('.swiper', {
      // Optional parameters
      direction: 'horizontal',
      loop: true,
    
      // If we need pagination
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
    
      // Navigation arrows
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    
      // And if we need scrollbar
      scrollbar: {
        el: '.swiper-scrollbar',
      },
    });
    }

    document.getElementById('openWebsiteBtn').addEventListener('click', function() {
      // Redirect to the specified website when the button is clicked
      window.open('http://127.0.0.1:5000/', '_blank');
  });
let currentIndex = 0;
const sliderWrapper = document.querySelector('.slider-wrapper');
const sliderItems = document.querySelectorAll('.section-item');
const totalSlides = sliderItems.length;

// Create dots dynamically based on the number of slides
const dotsContainer = document.createElement('div');
dotsContainer.classList.add('slider-dots');
sliderItems.forEach((_, index) => {
  const dot = document.createElement('span');
  dot.classList.add('slider-dot');
  if (index === 0) dot.classList.add('active'); // Make the first dot active
  dotsContainer.appendChild(dot);
});
document.querySelector('.slider-container').appendChild(dotsContainer);
const dots = document.querySelectorAll('.slider-dot');

function updateSlider() {
  const slideWidth = sliderItems[0].clientWidth;
  sliderWrapper.style.transform = `translateX(-${slideWidth * currentIndex}px)`;

  sliderItems.forEach((item, index) => {
    item.classList.remove('active'); // Remove active class from all items
    if (index === currentIndex) {
      item.classList.add('active'); // Add active class to the current item
      item.style.zIndex = 1;
    } else {
      item.style.zIndex = 0;
    }
  });

  dots.forEach((dot, index) => {
    dot.classList.remove('active');
    if (index === currentIndex) {
      dot.classList.add('active');
    }
  });
}

document.querySelector('.next').addEventListener('click', () => {
  if (currentIndex < totalSlides - 1) {
    currentIndex++;
  } else {
    currentIndex = 0;
  }
  updateSlider();
});

document.querySelector('.prev').addEventListener('click', () => {
  if (currentIndex > 0) {
    currentIndex--;
  } else {
    currentIndex = totalSlides - 1;
  }
  updateSlider();
});

// Automatic slide function
function autoSlide() {
  setInterval(() => {
    if (currentIndex < totalSlides - 1) {
      currentIndex++;
    } else {
      currentIndex = 0;
    }
    updateSlider();
  }, 3000); // Change slide every 3 seconds
}

autoSlide();

function nextStep(step) {
  if (validateStep(step - 1)) {
    var currentStep = document.querySelector(".step.active");
    var nextStep = document.getElementById("step-" + step);

    if (currentStep) {
      currentStep.classList.remove("active");
    }

    if (nextStep) {
      nextStep.classList.add("active");
    }
  }
}

function prevStep(step) {
  var currentStep = document.querySelector(".step.active");
  var prevStep = document.getElementById("step-" + step);

  if (currentStep) {
    currentStep.classList.remove("active");
  }

  if (prevStep) {
    prevStep.classList.add("active");
  }
}

function validateStep(step) {
  var valid = true;
  clearErrors();
  if (step === 1) {
    var lastName = document.getElementById("last-name").value;
    var firstName = document.getElementById("first-name").value;
    if (!lastName || !isNaN(lastName)) {
      document.getElementById("last-name-error").innerText =
        "Please enter a valid last name.";
      valid = false;
    }
    if (!firstName || !isNaN(firstName)) {
      document.getElementById("first-name-error").innerText =
        "Please enter a valid first name.";
      valid = false;
    }
  } else if (step === 2) {
    var month = document.getElementById("dob-month").value;
    var day = document.getElementById("dob-day").value;
    var year = document.getElementById("dob-year").value;
    var hour = document.getElementById("dob-hour").value;
    var minute = document.getElementById("dob-minute").value;
    if (
      !month ||
      isNaN(month) ||
      month < 1 ||
      month > 12 ||
      !day ||
      isNaN(day) ||
      day < 1 ||
      day > 31 ||
      !year ||
      isNaN(year) ||
      !hour ||
      isNaN(hour) ||
      hour < 0 ||
      hour > 23 ||
      !minute ||
      isNaN(minute) ||
      minute < 0 ||
      minute > 59
    ) {
      document.getElementById("dob-error").innerText =
        "Please enter a valid date and time.";
      valid = false;
    }
  } else if (step === 3) {
    var region = document.getElementById("region").value;
    var country = document.getElementById("country").value;
    if (!region || !isNaN(region)) {
      document.getElementById("location-error").innerText =
        "Please enter a valid region.";
      valid = false;
    }
    if (!country || !isNaN(country)) {
      document.getElementById("location-error").innerText =
        "Please enter a valid country.";
      valid = false;
    }
  } else if (step === 4) {
    var email = document.getElementById("email").value;
    if (!email || !validateEmail(email)) {
      document.getElementById("email-error").innerText =
        "Please enter a valid email address.";
      valid = false;
    }
  }
  return valid;
}

function clearErrors() {
  var errors = document.querySelectorAll(".error");
  errors.forEach(function (error) {
    error.innerText = "";
  });
}

function validateEmail(email) {
  var re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
  return re.test(email);
}

function submitForm() {
  if (validateStep(4)) {
    console.log("Validation passed");

    var formContainer = document.getElementById("form-container");
    var resultContainer = document.getElementById("result-container");

    if (!formContainer || !resultContainer) {
      console.error("Containers not found");
      return;
    }

    formContainer.style.display = "none";
    resultContainer.style.display = "block";

    var year = parseInt(document.getElementById("dob-year").value, 10);
    var element = "";
    var elementDescription = "";
    var elementImage = "";
    var elementSuggestions = "";

    if (year >= 1950 && year <= 1960) {
      element = "Yin Earth";
      elementDescription =
        "Nurturing, charismatic, peaceful: You are the soft soil of the garden.";
      elementImage =
        "https://www.theharmonist.eu/cdn/shop/files/harmonist-elements-page-earth-gif.gif?v=1615323006&width=714";
      elementSuggestions = `
        <p onclick="toggleDescription('socializing')">
          Socializing <span id="socializing-sign">+</span>
        </p>
        <div id="socializing-description" class="description">
          If you seek to turn on the charm, enhance your social life, make new friends, or unleash your networking potential, the Earth perfume is the scent for you. Earth reflects your own personal energy and since ‘like attracts like’ you will soon discover your more gregarious, social side. Using the Earth scent will make you more outgoing, spontaneous, and approachable. Your new infectious energy will bring out the best in those around you, too. As you enhance your people skills, others will be able to see things from your perspective.
        </div>
         <p onclick="toggleDescription('creativity')">
          creativity <span id="creativity-sign">+</span>
        </p>
        <div id="creativity-description" class="description">
        If you seek to introduce more fun, creativity, intelligence and passion into your life, then the Metal perfume is for you. Metal can be used to fashion beautiful things, so by surrounding yourself with the Metal scent, you can unlock your imagination, becoming more expressive, optimistic, confident and cheerful. You will find yourself centre stage with a renewed passion for life: curious, playful and ready for new challenges. Since your verbal skills will improve, too, you can market yourself more successfully as well.
        </div>
         <p onclick="toggleDescription('prosperity & seduction')">
          prosperity & seduction <span id="prosperity & seduction">+</span>
        </p>
        <div id="prosperity & seduction-description" class="description">
        Ever feel stuck in a rut? Then it’s time to tap into your Prosperity element, Water, to shake things up a little and take control. Your element, Earth, dams Water, so by harnessing the essence of Water, you will be able to take charge, becoming more assertive, efficient, dynamic and results-oriented. Enveloping yourself in the scent of Water will widen your vision, enabling you to focus on long-term goals. You will find yourself ready to take risks and longing for change. Financial success should soon follow, riding the tide of your newfound ambition and determination. So use the Water scent and watch your dreams come true!
        </div>
         <p onclick="toggleDescription('Status')">
          Status <span id="Status-sign">+</span>
        </p>
        <div id="Status-description" class="description">
        Your Status element is Wood, and since the roots of a strong tree can support an earthy bank, use the Earth scent if you seek new structure – or new companions - in your life. The Wood energy can boost your sex appeal, too, enhancing your powers of seduction and increasing your allure. Calm, steady and diplomatic, you will find yourself less influenced by your emotions, a good listener and peacekeeper. Since these are qualities your boss will appreciate, you may expect to see an improvement in your status soon, too.
        </div>
         <p onclick="toggleDescription('Wisdom')">
          Wisdom <span id="Wisdom-sign">+</span>
        </p>
        <div id="Wisdom-description" class="description">
        Fire is the molten core, the centre of the Earth, so if you seek to nourish body, soul and mind, envelope yourself in an aura of Fire. Its calming effect helps you relax so that your mind can become more reflective, analytical, attentive and methodical. Use Fire to unlock your abilities for problem-solving and research, and, better able to manage your time, your life will take on a more orderly, balanced harmony. Friends will turn to you for advice, appreciating your discreet loyalty and compassionate sincerity.
        </div>
      `;
    }
    if (year >= 1961 && year <= 1971) {
      element = "Yang Water";
      elementDescription =
        "active, intelligent, straightforward: You are the vast and powerful ocean.";
      elementImage =
        "https://www.theharmonist.eu/cdn/shop/files/harmonist-elements-page-water-gif.gif?v=1615323057&width=1000";
      elementSuggestions = `
        <p onclick="toggleDescription('socializing')">
          Socializing <span id="socializing-sign">+</span>
        </p>
        <div id="socializing-description" class="description">
          If you seek to turn on the charm, enhance your social life, make new friends, or unleash your networking potential, the Earth perfume is the scent for you. Earth reflects your own personal energy and since ‘like attracts like’ you will soon discover your more gregarious, social side. Using the Earth scent will make you more outgoing, spontaneous, and approachable. Your new infectious energy will bring out the best in those around you, too. As you enhance your people skills, others will be able to see things from your perspective.
        </div>
         <p onclick="toggleDescription('creativity')">
          creativity <span id="creativity-sign">+</span>
        </p>
        <div id="creativity-description" class="description">
        If you seek to introduce more fun, creativity, intelligence and passion into your life, then the Metal perfume is for you. Metal can be used to fashion beautiful things, so by surrounding yourself with the Metal scent, you can unlock your imagination, becoming more expressive, optimistic, confident and cheerful. You will find yourself centre stage with a renewed passion for life: curious, playful and ready for new challenges. Since your verbal skills will improve, too, you can market yourself more successfully as well.
        </div>
         <p onclick="toggleDescription('prosperity & seduction')">
          prosperity & seduction <span id="prosperity & seduction">+</span>
        </p>
        <div id="prosperity & seduction-description" class="description">
        Ever feel stuck in a rut? Then it’s time to tap into your Prosperity element, Water, to shake things up a little and take control. Your element, Earth, dams Water, so by harnessing the essence of Water, you will be able to take charge, becoming more assertive, efficient, dynamic and results-oriented. Enveloping yourself in the scent of Water will widen your vision, enabling you to focus on long-term goals. You will find yourself ready to take risks and longing for change. Financial success should soon follow, riding the tide of your newfound ambition and determination. So use the Water scent and watch your dreams come true!
        </div>
         <p onclick="toggleDescription('Status')">
          Status <span id="Status-sign">+</span>
        </p>
        <div id="Status-description" class="description">
        Your Status element is Wood, and since the roots of a strong tree can support an earthy bank, use the Earth scent if you seek new structure – or new companions - in your life. The Wood energy can boost your sex appeal, too, enhancing your powers of seduction and increasing your allure. Calm, steady and diplomatic, you will find yourself less influenced by your emotions, a good listener and peacekeeper. Since these are qualities your boss will appreciate, you may expect to see an improvement in your status soon, too.
        </div>
         <p onclick="toggleDescription('Wisdom')">
          Wisdom <span id="Wisdom-sign">+</span>
        </p>
        <div id="Wisdom-description" class="description">
        Fire is the molten core, the centre of the Earth, so if you seek to nourish body, soul and mind, envelope yourself in an aura of Fire. Its calming effect helps you relax so that your mind can become more reflective, analytical, attentive and methodical. Use Fire to unlock your abilities for problem-solving and research, and, better able to manage your time, your life will take on a more orderly, balanced harmony. Friends will turn to you for advice, appreciating your discreet loyalty and compassionate sincerity.
        </div>
      `;
    }
    if (year >= 1972 && year <= 1983) {
      element = "Yang Wood";
      elementDescription =
        "self-confident, helpful, principled: Like a tall tree, you are strong and your roots go deep.";
      elementImage =
        "https://www.theharmonist.eu/cdn/shop/files/harmonist-elements-page-wood-gif_06d5a34f-8630-400e-b6b0-c9eea96a73d7.gif?v=1615323244&width=1000";
      elementSuggestions = `
        <p onclick="toggleDescription('socializing')">
          Socializing <span id="socializing-sign">+</span>
        </p>
        <div id="socializing-description" class="description">
        If you seek to turn on the charm, enhance your social life, make new friends, or unleash your networking potential, the Wood perfume is the scent for you. Wood reflects your own personal energy and since ‘like attracts like,’ you will soon discover your more gregarious social side. Using the Wood scent will help you spread your branches, making you more out-going, spontaneous and approachable. Your new infectious energy will bring out the best in those around you, too. As you enhance your people skills, others will be able to see things from your perspective.
        </div>
         <p onclick="toggleDescription('creativity')">
          creativity <span id="creativity-sign">+</span>
        </p>
        <div id="creativity-description" class="description">
        If you seek to introduce more fun, creativity, intelligence and passion into your life, then the Fire perfume is for you. Your personal element, Wood, feeds Fire, so by surrounding yourself with its aura, you can unlock your imagination, becoming more expressive, optimistic, confident and cheerful. You will find yourself centre stage, radiating a renewed passion for life: curious, playful and ready for new challenges. Since your verbal skills will improve, too, you can market yourself more successfully as well.
        </div>
         <p onclick="toggleDescription('prosperity & seduction')">
          prosperity & seduction <span id="prosperity & seduction">+</span>
        </p>
        <div id="prosperity & seduction-description" class="description">
        Ever feel stuck in a rut? Then it’s time to tap into your Prosperity element to shake things up a little. Enveloping yourself in the scent of Earth will widen your vision, enabling you to focus on long-term goals. More ambitious, dynamic and assertive, you will find yourself ready to take risks and longing for change. Financial success should soon follow, riding the tide of your newfound determination and dedication. So use the Earth scent and watch your dreams come true!
        </div>
         <p onclick="toggleDescription('Status')">
          Status <span id="Status-sign">+</span>
        </p>
        <div id="Status-description" class="description">
        Your Status element is Metal, and although an axe can fell a tree, careful pruning can bring great results, so use the Metal scent if you seek new structure – or new companions - in your life. The Metal energy can boost your sex appeal, enhancing your powers of seduction and increasing your allure. Calm, steady and diplomatic, you will find yourself less influenced by your emotions, a good listener and peacekeeper. Since these are qualities your boss will appreciate, you may expect to see an improvement in your status soon, too.
        </div>
         <p onclick="toggleDescription('Wisdom')">
          Wisdom <span id="Wisdom-sign">+</span>
        </p>
        <div id="Wisdom-description" class="description">
        Water nourishes Wood, so if you seek to nourish body, soul and mind, surround yourself with the Water scent. Its calming effect helps you relax so that your mind can become more reflective, analytical, attentive and methodical. Use Water to unlock your abilities for problem-solving and research, and, better able to manage your time, your life will take on a more orderly, balanced harmony. Friends will turn to you for advice, appreciating your discreet loyalty and compassionate sincerity.
        </div>
      `;
    }
    if (year >= 1994 && year <= 2005) {
      element = "Yang Fire";
      elementDescription = "warm, friendly, open: You are the bright sun.";
      elementImage =
        "https://www.theharmonist.eu/cdn/shop/files/harmonist-elements-page-fire-gif.gif?v=1615323018&width=1280";
      elementSuggestions = `
        <p onclick="toggleDescription('socializing')">
          Socializing <span id="socializing-sign">+</span>
        </p>
        <div id="socializing-description" class="description">
        If you seek to turn on the charm, enhance your social life, make new friends, or unleash your networking potential, the Fire perfume is the scent for you. Fire reflects your own personal energy and since ‘like attracts like’ you will soon discover your more gregarious, social side. Using the Fire scent will make you more radiant, spontaneous and approachable. Your new infectious energy will bring out the best in those around you, too. As you enhance your people skills, others will be able to see things from your perspective.
        </div>
         <p onclick="toggleDescription('creativity')">
          creativity <span id="creativity-sign">+</span>
        </p>
        <div id="creativity-description" class="description">
        If you seek to introduce more fun, creativity, intelligence and passion into your life, then the Earth perfume is for you. Your personal element, Fire, is like Earth’s molten core, so by immersing yourself in its aura, you can unlock your imagination, becoming more expressive, optimistic, confident and cheerful. You will find yourself centre stage with a renewed passion for life: curious, playful and ready for new challenges. Since your verbal skills will improve, too, you can market yourself more successfully as well.
        </div>
         <p onclick="toggleDescription('prosperity & seduction')">
          prosperity & seduction <span id="prosperity & seduction">+</span>
        </p>
        <div id="prosperity & seduction-description" class="description">
        Ever feel stuck in a rut? Then it’s time to tap into your Prosperity element to shake things up a little. Enveloping yourself in the scent of mighty Metal will widen your vision, enabling you to focus on long-term goals. More ambitious, dynamic and assertive, you will find yourself ready to take risks and longing for change. Financial success should soon follow, riding the tide of your newfound determination and dedication. So use the Metal scent and watch your dreams come true!
        </div>
         <p onclick="toggleDescription('Status')">
          Status <span id="Status-sign">+</span>
        </p>
        <div id="Status-description" class="description">
        Your Status element is Water, and although Water can extinguish Fire, it can also control your more flammable nature, so use the Water scent if you seek new structure – or new companions - in your life. The Water energy can boost your sex appeal, enhancing your powers of seduction and increasing your allure. Calm, steady and diplomatic, you will find yourself less influenced by your emotions, a good listener and peacekeeper. Since these are qualities your boss will appreciate, you may expect to see an improvement in your status soon, too.



        </div>
         <p onclick="toggleDescription('Wisdom')">
          Wisdom <span id="Wisdom-sign">+</span>
        </p>
        <div id="Wisdom-description" class="description">
        Wood nourishes Fire, so if you seek to nourish body, soul and mind, surround yourself with the Wood scent. Its calming effect helps you relax so that your mind can become more reflective, analytical, attentive and methodical. Use Wood to unlock your abilities for problem-solving and research, and, better able to manage your time, your life will take on a more orderly, balanced harmony. Friends will turn to you for advice, appreciating your discreet loyalty and compassionate sincerity.
        </div>
      `;
    }
    if (year >= 2006 && year <= 2016) {
      element = "Yang Metal";
      elementDescription =
        "strong personality, resolute, loyal: You are the strong sword";
      elementImage =
        "https://www.theharmonist.eu/cdn/shop/files/harmonist-elements-page-metal-gif.gif?v=1615323035&width=1280";
      elementSuggestions = `
        <p onclick="toggleDescription('socializing')">
          Socializing <span id="socializing-sign">+</span>
        </p>
        <div id="socializing-description" class="description">
        If you seek to turn on the charm, enhance your social life, make new friends, or unleash your networking potential, the Metal perfume is the scent for you. Metal reflects your own personal energy and since ‘like attracts like’ you will soon discover your more gregarious, social side. Using the Metal scent will make you more out-going, spontaneous and approachable. Your new infectious energy will bring out the best in those around you, too. As you enhance your people skills, others will be able to see things from your perspective.
        </div>
         <p onclick="toggleDescription('creativity')">
          creativity <span id="creativity-sign">+</span>
        </p>
        <div id="creativity-description" class="description">
        If you seek to introduce more fun, creativity, intelligence and passion into your life, then the Water perfume is for you. Your personal element, Metal, gives shape to Water, so by wrapping yourself in the Water scent, you can open the floodgates of your imagination, becoming more expressive, optimistic, confident and cheerful. You will find yourself centre stage with a renewed passion for life: curious, playful and ready for new challenges. Since your verbal skills will improve, too, you can market yourself more successfully as well.
        </div>
         <p onclick="toggleDescription('prosperity & seduction')">
          prosperity & seduction <span id="prosperity & seduction">+</span>
        </p>
        <div id="prosperity & seduction-description" class="description">
        Ever feel stuck in a rut? Then it’s time to tap into your Prosperity element, Wood, to shake things up a little and take control. Your element, Metal, fells Wood, so by harnessing the essence of Wood, you will be able to take charge, becoming more assertive, efficient, dynamic and results-oriented. Enveloping yourself in the scent of Metal will widen your vision, enabling you to focus on long-term goals. You will find yourself ready to take risks and longing for change. Financial success should soon follow, riding the tide of your newfound ambition and determination. So use the Wood scent and watch your dreams come true!
        </div>
         <p onclick="toggleDescription('Status')">
          Status <span id="Status-sign">+</span>
        </p>
        <div id="Status-description" class="description">
        Your Status element is Fire, and although fire melts metal, it is also used to fashion great monuments, so use the Fire scent if you seek promotion or new structure in your life. Calm, steady and diplomatic, you will find yourself less influenced by your emotions, a better listener and peacekeeper. Since these are qualities your boss will appreciate, thanks to your increased integrity and reliability, you may expect to see an improvement in your status soon, too.
        </div>
         <p onclick="toggleDescription('Wisdom')">
          Wisdom <span id="Wisdom-sign">+</span>
        </p>
        <div id="Wisdom-description" class="description">
        For you, Wood represents Seduction and Prosperity. Your element, Metal, fells Wood, so why not axe your obstacles and take control of your love life as well as your finances? The essence of Wood will enhance your seductive powers, magnetizing women to your irresistible charm. You will also find yourself better able to take charge, becoming more assertive, efficient, dynamic and results-oriented. More ambitious and competitive, you will find yourself ready to take risks and longing for change.
        </div>
      `;
    }
    if (year >= 2017 && year <= 2027) {
      element = "Yin Water";
      elementDescription =
        "gentle, peaceful, patient: You are the drop of water, the morning dew.";
      elementImage =
        "https://www.theharmonist.eu/cdn/shop/files/harmonist-elements-page-water-gif.gif?v=1615323057&width=1000";
      elementSuggestions = `
        <p onclick="toggleDescription('socializing')">
          Socializing <span id="socializing-sign">+</span>
        </p>
        <div id="socializing-description" class="description">
        If you seek to turn on the charm, enhance your social life, make new friends, or unleash your networking potential, the Water perfume is the scent for you. Water reflects your own personal energy and since ‘like attracts like’ you will soon discover your more gregarious, social side. Use the Water scent to unlock your out-going, spontaneous and approachable side. Your new infectious energy will bring out the best in those around you, too. As you enhance your people skills, others will be able to see things from your perspective.
        </div>
         <p onclick="toggleDescription('creativity')">
          creativity <span id="creativity-sign">+</span>
        </p>
        <div id="creativity-description" class="description">
        If you seek to introduce more fun, creativity, intelligence and passion into your life, then the Wood perfume is for you. Your Creativity element, Wood, relies on your personal element, Water, for growth so by immersing yourself in this scent, you can unlock your imagination, becoming more expressive, optimistic, confident and cheerful. You will find yourself centre stage with a renewed passion for life: curious, playful and ready for new challenges. Since your verbal skills will improve, too, you can market yourself more successfully as well.
        </div>
         <p onclick="toggleDescription('prosperity & seduction')">
          prosperity & seduction <span id="prosperity & seduction">+</span>
        </p>
        <div id="prosperity & seduction-description" class="description">
        Ever feel stuck in a rut? Then it’s time to tap into your Prosperity element, Fire, to shake things up a little and take control. Fire is at the mercy of your element, Water, so harnessing the essence of Fire, will empower you to take charge, becoming more assertive, efficient, dynamic and results-oriented. Enveloping yourself in the scent of Fire will widen your vision, enabling you to focus on long-term goals. You will find yourself ready to take risks and longing for change. Financial success should soon follow, riding the tide of your newfound ambition and determination. So use the Fire scent and watch your dreams come true!
        </div>
         <p onclick="toggleDescription('Status')">
          Status <span id="Status-sign">+</span>
        </p>
        <div id="Status-description" class="description">
        Your Status element is Earth, and since Earth can dam and channel your element, Water, use the aroma of Earth if you seek new structure – or new companions - in your life. The Earth energy can boost your sex appeal, too, enhancing your powers of seduction and increasing your allure. Calm, steady and diplomatic, you will find yourself less influenced by your emotions, a good listener and peacekeeper. Since these are qualities your boss will appreciate, you may expect to see an improvement in your status soon, too.
        </div>
         <p onclick="toggleDescription('Wisdom')">
          Wisdom <span id="Wisdom-sign">+</span>
        </p>
        <div id="Wisdom-description" class="description">
        Minerals – Metal – give Water special healing properties, so if you seek to nourish body, soul and mind, envelope yourself in your Resource element, Metal. Its calming effect helps you relax so that your mind can become more reflective, analytical, attentive and methodical. Use Metal to unlock your abilities for problem-solving and research, and, better able to manage your time, your life will take on a more orderly, balanced harmony. Friends will turn to you for advice, appreciating your discreet loyalty and compassionate sincerity.
        </div>
      `;
    }

    var elementName = document.getElementById("element-name");
    var elementImageElem = document.getElementById("element-image");
    var elementDescriptionElem = document.getElementById("element-description");
    var resultDetailsElem = document.getElementById("result-details");

    if (elementName) elementName.innerText = element;
    if (elementImageElem) {
      elementImageElem.src = elementImage;
      elementImageElem.onerror = function () {
        console.error("Failed to load image:", elementImage);
      };
    }
    if (elementDescriptionElem)
      elementDescriptionElem.innerText = elementDescription;
    if (resultDetailsElem) resultDetailsElem.innerHTML = elementSuggestions;

    console.log("Element Name:", element);
    console.log("Element Image:", elementImage);
    console.log("Element Description:", elementDescription);
    console.log("Element Suggestions:", elementSuggestions);
  }
}

function toggleDescription(id) {
  const description = document.getElementById(`${id}-description`);
  const sign = document.getElementById(`${id}-sign`);

  if (description.style.display === "block") {
    description.style.display = "none";
    sign.textContent = "+";
  } else {
    description.style.display = "block";
    sign.textContent = "-";
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const accordions = document.querySelectorAll(".accordion-button");
  accordions.forEach((button) => {
    button.addEventListener("click", function () {
      console.log("Accordion button clicked");
      const content = this.nextElementSibling;
      this.classList.toggle("active");
      const icon = this.querySelector(".iconplus");

      if (content.style.maxHeight) {
        content.style.maxHeight = null;
        icon.classList.remove("fa-minus");
        icon.classList.add("fa-plus");
      } else {
        content.style.maxHeight = content.scrollHeight + "px";
        icon.classList.remove("fa-plus");
        icon.classList.add("fa-minus");
      }
    });
  });
});

let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides((slideIndex += n));
}

function currentSlide(n) {
  showSlides((slideIndex = n));
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
}

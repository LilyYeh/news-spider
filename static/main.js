function setTab(category) {
  sessionStorage.setItem('selectedTab', category);
}

window.onload = function() {
  const tab = sessionStorage.getItem('selectedTab');
  if (tab) {
	  $('#' + tab + "-tab").addClass('active');
	  $('#' + tab).addClass('show active');
  } else {
	  $('#top-tab').addClass('active');
	  $('#top').addClass('show active');
  }
};

document.addEventListener("DOMContentLoaded", function () {
    const nav = document.getElementById("myTab");
    const placeholder = document.getElementById("navPlaceholder");
    const offsetTop = nav.offsetTop;

    window.addEventListener("scroll", function () {
        if (window.pageYOffset >= offsetTop) {
            nav.classList.add("sticky-nav");
            placeholder.style.display = "block";
        } else {
            nav.classList.remove("sticky-nav");
            placeholder.style.display = "none";
        }
    });
});
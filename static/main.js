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
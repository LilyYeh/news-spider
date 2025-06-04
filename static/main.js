function setTab(category) {
    sessionStorage.setItem('selectedTab', category);
}

$(document).ready(function () {
    // 頁面載入後，填入更新時間
    $('.last-update-time span').text(nowDateTime());

    // 頁面載入後設定選中的 Tab
    const tab = sessionStorage.getItem('selectedTab');
    if (tab) {
        $('#' + tab + "-tab").addClass('active');
        $('#' + tab).addClass('show active');
    } else {
        $('#top-tab').addClass('active');
        $('#top').addClass('show active');
    }

    // Sticky 導覽列
    const $nav = $("#myTab");
    const $placeholder = $("#navPlaceholder");
    const offsetTop = $nav.offset().top;

    $(window).on("scroll", function () {
        if ($(window).scrollTop() >= offsetTop) {
            $nav.addClass("sticky-nav");
            $placeholder.show();
        } else {
            $nav.removeClass("sticky-nav");
            $placeholder.hide();
        }
    });

    function nowDateTime() {
        const now = new Date();
        const taipeiTime = new Date(
            now.toLocaleString("en-US", {timeZone: "Asia/Taipei"})
        );

        const year = taipeiTime.getFullYear();
        const month = String(taipeiTime.getMonth() + 1).padStart(2, '0');
        const day = String(taipeiTime.getDate()).padStart(2, '0');
        const hours = String(taipeiTime.getHours()).padStart(2, '0');
        const minutes = String(taipeiTime.getMinutes()).padStart(2, '0');
        const seconds = String(taipeiTime.getSeconds()).padStart(2, '0');

        return `${year}/${month}/${day} ${hours}:${minutes}:${seconds}`;
    }


    let isOpen = false;
    const ettodayWrapper = '.ettoday-wrapper';
    const collapseBtn = '.collapse-btn';
    const collapseWrapper = '.collapse-wrapper';

    $(collapseBtn).on('click', function () {
        switchCollapseWrapper();
    });

    function switchCollapseWrapper() {
        if (isOpen) {
            openCollapseWrapper();
            isOpen = false;
        } else {
            closeAllCollapseWrapper();
            isOpen = true;
        }
    }

    function openCollapseWrapper() {
        $(ettodayWrapper).removeClass('collapsed');
        //$(collapseWrapper).css('height', 'auto');
    }

    function closeAllCollapseWrapper() {
        $(ettodayWrapper).addClass('collapsed')
    }
});
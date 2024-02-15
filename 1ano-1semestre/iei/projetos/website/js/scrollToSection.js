function scrollToSection(sectionId) {
    var offset = $('#' + sectionId).offset().top;
    $('html, body').animate({
        scrollTop: offset
    }, 1000);
}

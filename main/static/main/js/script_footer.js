$(document).ready(function()
{
    $('.h4').click(function(event)
    {
        if($('.container').hasClass('con1'))
        {
            $('.h4').not($(this)).removeClass('active');
            $('.aaa').not($(this).next()).slideUp(300);
            $('.blogs').not($(this).next()).slideUp(300);
            $('.insta').not($(this).next()).slideUp(300);
        }
        
        $(this).toggleClass('active').next().slideToggle(300);
    });
});
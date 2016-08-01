$(document).ready(function(){
    $('a.selected').on('click',function(){
        $('.main').hide().load("public/html/create_user.html");
    });
});

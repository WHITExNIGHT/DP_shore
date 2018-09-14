jQuery(document).ready(function () {

    /*
        Fullscreen background
    */
    $.backstretch("/static/dp_user/img/backgrounds/b.png");

    /*
        Form validation
    */
    // $('.login-form input[type="text"], .login-form input[type="password"], .login-form textarea').on('focus', function() {
    // 	$(this).removeClass('input-error');
    // });
    //
    // $('.login-form').on('submit', function(e) {
    //
    // 	$(this).find('input[type="text"], input[type="password"], textarea').each(function(){
    // 		if( $(this).val() == "" ) {
    // 			e.preventDefault();
    // 			$(this).addClass('input-error');
    // 		}
    // 		else {
    // 			$(this).removeClass('input-error');
    // 		}
    // 	});
    //
    // });


    $('.name_input').blur(function () {
        if ($('.name_input').val().length == 0) {
            $('.user_error').html('请填写用户名').show();
        }
    });

    $('.pass_input').blur(function () {
        if ($(this).val().length == 0) {
            $('.pwd_error').html('请输入密码').show();
        } else {
            $('.pwd_error').hide();
        }
    });
});

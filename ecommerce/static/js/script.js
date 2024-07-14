// some scripts

// jquery ready start
$(document).ready(function () {
    // jQuery code


    /* ///////////////////////////////////////

    THESE FOLLOWING SCRIPTS ONLY FOR BASIC USAGE, 
    For sliders, interactions and other

    */ ///////////////////////////////////////


    //////////////////////// Prevent closing from click inside dropdown
    $(document).on('click', '.dropdown-menu', function (e) {
        e.stopPropagation();
    });


    $('.js-check :radio').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $('input[name=' + check_attr_name + ']').closest('.js-check').removeClass('active');
            $(this).closest('.js-check').addClass('active');
            // item.find('.radio').find('span').text('Add');

        } else {
            item.removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });


    $('.js-check :checkbox').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $(this).closest('.js-check').addClass('active');
            // item.find('.radio').find('span').text('Add');
        } else {
            $(this).closest('.js-check').removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });


    //////////////////////// Bootstrap tooltip
    if ($('[data-toggle="tooltip"]').length > 0) {  // check if element exists
        $('[data-toggle="tooltip"]').tooltip()
    } // end if

    //DYNAMIC GREETING MESSAGE START========================
    let datetime = new Date(),
        h = datetime.getHours(),
        greeting, emoji;
    if (5 <= h && h < 12) {
        greeting = 'Good Morning';
        emoji = '☀️'; // Sun emoji
    } else if (12 <= h && h < 18) {
        greeting = 'Good Afternoon';
        emoji = '🌞'; // Sun with face emoji
    } else if (18 <= h && h < 22) {
        greeting = 'Good Evening';
        emoji = '🌆'; // Cityscape at dusk emoji
    } else {
        greeting = 'Good Night';
        emoji = '🌙'; // Crescent moon emoji
    }
    $('#greetings').text(`${greeting} ${emoji}`);

    //DYNAMIC GREETING MESSAGE END========================
    setTimeout(function () {
        $(".alert").alert('close')
    }, 5000);


});
// jquery end


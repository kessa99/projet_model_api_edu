
$('.like-button').click(function () {
    var bourseId = $(this).data('bourse-id');

    // Envoyer une demande à notre serveur pour dire que nous aimons ou n'aimons pas cet article
    $.ajax({
        type: 'POST',
        url: '/toggle_like/' + bourseId + '/',
        data: {'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()},
        success: function (data) {
            // Mettre à jour le nombre total de "likes"
            $('.like-count').text(data.like_count);
        }
    });
});

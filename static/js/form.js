$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				username : $('#usernameInput').val(),
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text((function() {
					return "Hello " + ( data.username );
				  })).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});
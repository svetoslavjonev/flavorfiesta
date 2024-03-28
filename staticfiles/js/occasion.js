document.addEventListener('DOMContentLoaded', function() {

	document.querySelectorAll('.occasion-form input, .occasion-form select').forEach(function(input) {
		input.addEventListener('change', function() {

			document.getElementById('occasionForm').submit();
		});
	});
});
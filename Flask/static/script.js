$(document).ready(function() {
    $('#sentimentForm').submit(function(event) {
        event.preventDefault();
        
        // Get input text
        var text = $('#textInput').val();
        
        // Send POST request to server
        $.ajax({
            type: 'POST',
            url: '/analyze',
            contentType: 'application/x-www-form-urlencoded',
            data: {text: text},
            success: function(response) {
                // Display sentiment analysis result
                $('#result').text('Overall sentiment: ' + response.sentiment);
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });
});

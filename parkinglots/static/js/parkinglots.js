$(document).ready(function() {
    $('#table-parking-lots').DataTable({
        'lengthChange': false,
        'searching': false
    });

    $('#add-parking-lot').click(function() {
        $('#view-add-parking-lot').removeClass('hidden').removeAttr('style');
    });
});


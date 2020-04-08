
function confirmDeleteModal(id) {
 $('#deleteModal').modal();
 $('#deleteButton').html('<a href="/removeentry/?id='+id+'" class="btn btn-danger" onclick="return closeDeleteModal('+id+')">Delete</a>');
}


function closeDeleteModal(id) {
 $('#deleteModal').modal('hide');
 return true
}
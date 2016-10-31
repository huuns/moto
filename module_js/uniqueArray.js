// =============================================================================
// write      : moto
// update     : 2016.10.31.
// duplicate array to unique array
// =============================================================================




var uniqueArray = function(duplicateArrary) {
    var uniqueElements = [];
    $.each(duplicateArrary, function(i, element) {
        if ($.inArray(element, uniqueElements) === -1) uniqueElements.push(element);
    });
    return uniqueElements.sort();
};

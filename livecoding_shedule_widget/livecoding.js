var livecoding = function() {

    var options = function() {

    };

    function publicRender() {
        console.log('public render loaded');
    }


    return {
        render: publicRender
    };
}();
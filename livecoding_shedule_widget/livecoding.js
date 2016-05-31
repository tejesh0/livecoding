var livecoding = function() {

    var options = function() {

    };

    function publicRender() {
        livecodingDiv = document.createElement('div');

        livecodingDiv.id = "livecoding";

        livecodingDiv.innerHTML = '<p>' + schedule.topic + ' : ' + schedule.title + '---' + schedule.time + '</p>';

        document.getElementsByTagName('body')[0].appendChild(livecodingDiv);
    }


    return {
        render: publicRender
    };
}();
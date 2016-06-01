var livecoding = function() {

    var options = function() {

    };

    function fetch_my_schedules() {
        // fetch access token of particular user
        // user name is fetched from input text box
        var username = "tejesh95";
        xhttp.open("GET", "http://localhost:5000/livecoding/schedules/" + username + "/", true);

        xhttp.send();

        xhttp.onreadystatechange = function() {
            if (xhttp.readystate == 4 && xhttp.status == 200) {
                alert("sucess everywhere!!");
            } else {
                alert("careful mooore");
            }
        };

    }

    function publicRender() {
        livecodingDiv = document.createElement('div');

        shcedules = fetch_my_schedules();
        console.log(schedules);

        livecodingDiv.id = "livecoding";

        livecodingDiv.innerHTML = '<p>' + schedule.topic + ' : ' + schedule.title + '---' + schedule.time + '</p>';

        document.getElementsByTagName('body')[0].appendChild(livecodingDiv);
    }


    return {
        render: publicRender
    };
}();
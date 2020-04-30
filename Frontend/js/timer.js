function AdjustingInterval(workFunc, interval, errorFunc) {
    var that = this;
    var expected, timeout;
    this.interval = interval;

    this.start = function() {
        expected = Date.now() + this.interval;
        timeout = setTimeout(step, this.interval);
    }

    this.stop = function() {
        clearTimeout(timeout);
    }

    function step() {
        var drift = Date.now() - expected;
        if (drift > that.interval) {
            // You could have some default stuff here too...
            if (errorFunc) errorFunc();
        }
        workFunc();
        expected += that.interval;
        timeout = setTimeout(step, Math.max(0, that.interval-drift));
    }
}

window.onload = mainfunc;
function mainfunc(){
    time = 0
    var intervalTask = function() {
        ++time
        digidisplay = new Date(time * 1000).toISOString().substr(11, 8);
        try{
            document.getElementById('time').innerHTML = digidisplay;
        }
        catch{
            timer.stop();
        }
    }
    var timer = new AdjustingInterval(intervalTask, 1000);
    timer.start();
}
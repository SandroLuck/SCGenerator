pragma solidity ^0.4.11;


contract owned {
    //This is an official solidity snippet from http://solidity.readthedocs.io/en/develop/contracts.html
    function owned() {owner = msg.sender;}

    address owner;
    // This contract only defines a modifier but does not use
    // it - it will be used in derived contracts.
    // The function body is inserted where the special symbol
    // This means that if the owner calls this function, the
    // function is executed and otherwise, an exception is
    // thrown.
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }
}


contract iscoolingtruckontrack is owned {
    int16 constant HumidityRelativePercentLT = 15;

    int16 constant HumidityRelativePercentUT = 25;

    int16 constant TemperatureCelsiusLT = 0;

    int16 constant TemperatureCelsiusUT = 5;

    int16 constant TemperatureKelvinLT = 273;

    int16 constant TemperatureKelvinUT = 278;

    int16 constant longitudeDeciMilleLT = 430000;

    int16 constant longitudeDeciMilleUT = 450000;

    int16 constant latitudeDeciMilleLT = 440000;

    int16 constant latitudeDeciMilleUT = 460000;

    event AlarmHumidityRelativePercent(int16 _valHumidityRelativePercent, string _id);

    event AlarmTemperatureCelsius(int16 _valTemperatureCelsius, string _id);

    event AlarmTemperatureKelvin(int16 _valTemperatureKelvin, string _id);

    event AlarmlongitudeDeciMille(int16 _vallongitudeDeciMille, string _id);

    event AlarmlatitudeDeciMille(int16 _vallatitudeDeciMille, string _id);

    event AlarmAll(
    int16 _valHumidityRelativePercent, int16 _valTemperatureCelsius, int16 _valTemperatureKelvin, int16 _vallongitudeDeciMille, int16 _vallatitudeDeciMille, string _id
    );
    //The values returned by this function have the same order as the values listed at the beginning of this Smart Contract
    function getTriggers() constant onlyOwner
    returns (
    int16 HumidityRelativePercentLT, int16 HumidityRelativePercentUT, int16 TemperatureCelsiusLT, int16 TemperatureCelsiusUT, int16 TemperatureKelvinLT, int16 TemperatureKelvinUT, int16 longitudeDeciMilleLT, int16 longitudeDeciMilleUT, int16 latitudeDeciMilleLT, int16 latitudeDeciMilleUT){
        return (15, 25, 0, 5, 273, 278, 430000, 450000, 440000, 460000);}

    function updateHumidityRelativePercent(int16 _valHumidityRelativePercent, string _id) onlyOwner {if (HumidityRelativePercentLT > _valHumidityRelativePercent || HumidityRelativePercentUT < _valHumidityRelativePercent) {AlarmHumidityRelativePercent(_valHumidityRelativePercent, _id);}}

    function updateTemperatureCelsius(int16 _valTemperatureCelsius, string _id) onlyOwner {if (TemperatureCelsiusLT > _valTemperatureCelsius || TemperatureCelsiusUT < _valTemperatureCelsius) {AlarmTemperatureCelsius(_valTemperatureCelsius, _id);}}

    function updateTemperatureKelvin(int16 _valTemperatureKelvin, string _id) onlyOwner {if (TemperatureKelvinLT > _valTemperatureKelvin || TemperatureKelvinUT < _valTemperatureKelvin) {AlarmTemperatureKelvin(_valTemperatureKelvin, _id);}}

    function updatelongitudeDeciMille(int16 _vallongitudeDeciMille, string _id) onlyOwner {if (longitudeDeciMilleLT > _vallongitudeDeciMille || longitudeDeciMilleUT < _vallongitudeDeciMille) {AlarmlongitudeDeciMille(_vallongitudeDeciMille, _id);}}

    function updatelatitudeDeciMille(int16 _vallatitudeDeciMille, string _id) onlyOwner {if (latitudeDeciMilleLT > _vallatitudeDeciMille || latitudeDeciMilleUT < _vallatitudeDeciMille) {AlarmlatitudeDeciMille(_vallatitudeDeciMille, _id);}}

    function updateAll(
    int16 _valHumidityRelativePercent, int16 _valTemperatureCelsius, int16 _valTemperatureKelvin, int16 _vallongitudeDeciMille, int16 _vallatitudeDeciMille, string _id
    ) onlyOwner
    {
        if (
        (HumidityRelativePercentLT > _valHumidityRelativePercent || HumidityRelativePercentUT < _valHumidityRelativePercent) &&
        (TemperatureCelsiusLT > _valTemperatureCelsius || TemperatureCelsiusUT < _valTemperatureCelsius) &&
        (TemperatureKelvinLT > _valTemperatureKelvin || TemperatureKelvinUT < _valTemperatureKelvin) &&
        (longitudeDeciMilleLT > _vallongitudeDeciMille || longitudeDeciMilleUT < _vallongitudeDeciMille) &&
        (latitudeDeciMilleLT > _vallatitudeDeciMille || latitudeDeciMilleUT < _vallatitudeDeciMille)
        ) {
            AlarmAll(_valHumidityRelativePercent, _valTemperatureCelsius, _valTemperatureKelvin, _vallongitudeDeciMille, _vallatitudeDeciMille, _id);
        }
        else {
            if (HumidityRelativePercentLT > _valHumidityRelativePercent || HumidityRelativePercentUT < _valHumidityRelativePercent) {AlarmHumidityRelativePercent(_valHumidityRelativePercent, _id);}
            if (TemperatureCelsiusLT > _valTemperatureCelsius || TemperatureCelsiusUT < _valTemperatureCelsius) {AlarmTemperatureCelsius(_valTemperatureCelsius, _id);}
            if (TemperatureKelvinLT > _valTemperatureKelvin || TemperatureKelvinUT < _valTemperatureKelvin) {AlarmTemperatureKelvin(_valTemperatureKelvin, _id);}
            if (longitudeDeciMilleLT > _vallongitudeDeciMille || longitudeDeciMilleUT < _vallongitudeDeciMille) {AlarmlongitudeDeciMille(_vallongitudeDeciMille, _id);}
            if (latitudeDeciMilleLT > _vallatitudeDeciMille || latitudeDeciMilleUT < _vallatitudeDeciMille) {AlarmlatitudeDeciMille(_vallatitudeDeciMille, _id);}
        }
    }
}

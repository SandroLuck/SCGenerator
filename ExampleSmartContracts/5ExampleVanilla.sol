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
    event TemperatureCelsius(int16 _valTemperatureCelsius, string _id);

    event TemperatureKelvin(int16 _valTemperatureKelvin, string _id);

    event HumidityRelativePercent(int16 _valHumidityRelativePercent, string _id);

    event latitudeDeciMille(int16 _vallatitudeDeciMille, string _id);

    event longitudeDeciMille(int16 _vallongitudeDeciMille, string _id);

    event AlarmAll(
    int16 _valTemperatureCelsius, int16 _valTemperatureKelvin, int16 _valHumidityRelativePercent, int16 _vallatitudeDeciMille, int16 _vallongitudeDeciMille, string _id
    );

    function alarmTemperatureCelsius(int16 _valTemperatureCelsius, string _id) onlyOwner {TemperatureCelsius(_valTemperatureCelsius, _id);}

    function alarmTemperatureKelvin(int16 _valTemperatureKelvin, string _id) onlyOwner {TemperatureKelvin(_valTemperatureKelvin, _id);}

    function alarmHumidityRelativePercent(int16 _valHumidityRelativePercent, string _id) onlyOwner {HumidityRelativePercent(_valHumidityRelativePercent, _id);}

    function alarmlatitudeDeciMille(int16 _vallatitudeDeciMille, string _id) onlyOwner {latitudeDeciMille(_vallatitudeDeciMille, _id);}

    function alarmlongitudeDeciMille(int16 _vallongitudeDeciMille, string _id) onlyOwner {longitudeDeciMille(_vallongitudeDeciMille, _id);}

    function alarmAll(
    int16 _valTemperatureCelsius, int16 _valTemperatureKelvin, int16 _valHumidityRelativePercent, int16 _vallatitudeDeciMille, int16 _vallongitudeDeciMille, string _id
    ) onlyOwner
    {
        AlarmAll(_valTemperatureCelsius, _valTemperatureKelvin, _valHumidityRelativePercent, _vallatitudeDeciMille, _vallongitudeDeciMille, _id);
    }
}
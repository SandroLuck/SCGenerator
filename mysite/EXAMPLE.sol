pragma solidity ^0.4.11;


contract owned {
    //This is an official solidity snippet from
    //http://solidity.readthedocs.io/en/develop/contracts.html
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


contract roomtemperatureisok is owned {
    event TemperatureCelsiusPerCent(
    int16 _valTemperatureCelsiusPerCent,
    string _id);

    event RelativeHumidityInPerMille(
    int16 _valRelativeHumidityInPerMille,
    string _id);

    event AlarmAll(
    int16 _valTemperatureCelsiusPerCent,
    int16 _valRelativeHumidityInPerMille,
    string _id
    );

    function alarmTemperatureCelsiusPerCent(
    int16 _valTemperatureCelsiusPerCent,
    string _id
    ) onlyOwner {
        TemperatureCelsiusPerCent(_valTemperatureCelsiusPerCent, _id);
    }

    function alarmRelativeHumidityInPerMille(
    int16 _valRelativeHumidityInPerMille,
    string _id) onlyOwner {
        RelativeHumidityInPerMille(_valRelativeHumidityInPerMille, _id);
    }

    function alarmAll(
    int16 _valTemperatureCelsiusPerCent,
    int16 _valRelativeHumidityInPerMille,
    string _id
    ) onlyOwner
    {
        AlarmAll(_valTemperatureCelsiusPerCent, _valRelativeHumidityInPerMille, _id);
    }
}

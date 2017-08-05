pragma solidity ^0.4.11;
contract owned {
  //This is an official solidity snippet from http://solidity.readthedocs.io/en/develop/contracts.html
    function owned() { owner = msg.sender; }
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
contract welcome is owned {
		event TemperatureCelsius(int16 _valTemperatureCelsius,string _id);
    event AlarmAll(
			 int16 _valTemperatureCelsius, string _id
    );
		function alarmTemperatureCelsius(int16 _valTemperatureCelsius,string _id) onlyOwner{TemperatureCelsius(_valTemperatureCelsius, _id);}
    function alarmAll(
				int16 _valTemperatureCelsius, string _id
      ) onlyOwner
      {
				AlarmAll( _valTemperatureCelsius, _id);
      }
}

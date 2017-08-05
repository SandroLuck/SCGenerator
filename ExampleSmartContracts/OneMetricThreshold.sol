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
		int16 TemperatureCelsiusLT =35;
		int16 TemperatureCelsiusUT =50;

		event AlarmTemperatureCelsius(int16 _valTemperatureCelsius,string _id);

    event AlarmAll(
		 int16 _valTemperatureCelsius, string _id
    );
    function getTriggers()onlyOwner
    returns(
		int16 TemperatureCelsiusLT ,int16 TemperatureCelsiusUT    ){
		return(		TemperatureCelsiusLT , TemperatureCelsiusUT);    }
		function updateTemperatureCelsius(int16 _valTemperatureCelsius,string _id) onlyOwner{if(TemperatureCelsiusLT > _valTemperatureCelsius || TemperatureCelsiusUT < _valTemperatureCelsius){AlarmTemperatureCelsius(_valTemperatureCelsius, _id);}}
    function updateAll(
			int16 _valTemperatureCelsius, string _id
    ) onlyOwner
    {
      if(
			(TemperatureCelsiusLT > _valTemperatureCelsius || TemperatureCelsiusUT < _valTemperatureCelsius)
      ){
				AlarmAll( _valTemperatureCelsius, _id);
       }
       else{
			if(TemperatureCelsiusLT > _valTemperatureCelsius || TemperatureCelsiusUT < _valTemperatureCelsius){AlarmTemperatureCelsius(_valTemperatureCelsius, _id);}
       }
    }
}

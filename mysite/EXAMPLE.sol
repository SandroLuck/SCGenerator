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
contract roomtemperatureisok is owned {
		int16 TemperatureCelsiusPerCentLT =1800;
		int16 TemperatureCelsiusPerCentUT =2500;
		int16 RelativeHumidityInPerMilleLT =350;
		int16 RelativeHumidityInPerMilleUT =550;

		event AlarmTemperatureCelsiusPerCent(int16 _valTemperatureCelsiusPerCent,string _id);
		event AlarmRelativeHumidityInPerMille(int16 _valRelativeHumidityInPerMille,string _id);

    event AlarmAll(
		 int16 _valTemperatureCelsiusPerCent, int16 _valRelativeHumidityInPerMille, string _id
    );
    function getTriggers()onlyOwner
    returns(
		int16 TemperatureCelsiusPerCentLT ,int16 TemperatureCelsiusPerCentUT ,		int16 RelativeHumidityInPerMilleLT ,int16 RelativeHumidityInPerMilleUT    ){
		return(		TemperatureCelsiusPerCentLT , TemperatureCelsiusPerCentUT ,		RelativeHumidityInPerMilleLT , RelativeHumidityInPerMilleUT);    }
		function updateTemperatureCelsiusPerCent(int16 _valTemperatureCelsiusPerCent,string _id) onlyOwner{if(TemperatureCelsiusPerCentLT > _valTemperatureCelsiusPerCent || TemperatureCelsiusPerCentUT < _valTemperatureCelsiusPerCent){AlarmTemperatureCelsiusPerCent(_valTemperatureCelsiusPerCent, _id);}}
		function updateRelativeHumidityInPerMille(int16 _valRelativeHumidityInPerMille,string _id) onlyOwner{if(RelativeHumidityInPerMilleLT > _valRelativeHumidityInPerMille || RelativeHumidityInPerMilleUT < _valRelativeHumidityInPerMille){AlarmRelativeHumidityInPerMille(_valRelativeHumidityInPerMille, _id);}}
    function updateAll(
			int16 _valTemperatureCelsiusPerCent,int16 _valRelativeHumidityInPerMille, string _id
    ) onlyOwner
    {
      if(
			(TemperatureCelsiusPerCentLT > _valTemperatureCelsiusPerCent || TemperatureCelsiusPerCentUT < _valTemperatureCelsiusPerCent) &&
			(RelativeHumidityInPerMilleLT > _valRelativeHumidityInPerMille || RelativeHumidityInPerMilleUT < _valRelativeHumidityInPerMille)
      ){
				AlarmAll( _valTemperatureCelsiusPerCent, _valRelativeHumidityInPerMille, _id);
       }
       else{
			if(TemperatureCelsiusPerCentLT > _valTemperatureCelsiusPerCent || TemperatureCelsiusPerCentUT < _valTemperatureCelsiusPerCent){AlarmTemperatureCelsiusPerCent(_valTemperatureCelsiusPerCent, _id);}
			if(RelativeHumidityInPerMilleLT > _valRelativeHumidityInPerMille || RelativeHumidityInPerMilleUT < _valRelativeHumidityInPerMille){AlarmRelativeHumidityInPerMille(_valRelativeHumidityInPerMille, _id);}
       }
    }
}

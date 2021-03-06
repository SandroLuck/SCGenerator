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
contract @contractName@ is owned {
    @tresholdsInit@

    @singleEvents@

    event AlarmAll(
    @paramsAlarmAll@
    );
    //The values returned by this function have the same order as the values listed at the beginning of this Smart Contract
    function getTriggers() constant onlyOwner
    returns(
    @triggerReturns@
    ){
    @triggerRealReturn@
    }
    @singleUpdate@
    function updateAll(
        @paramsUpdateAll@
    ) onlyOwner
    {
      if(
      @codeUpdateAllIf@

      ){
       @codeUpdateAll@
       }
       else{
       @codeUpdateAllElse@
       }
    }
}

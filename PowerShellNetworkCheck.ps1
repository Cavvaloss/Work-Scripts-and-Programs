#Script that monitors standardized Intel Adapter. It will restart if it notices connection drop. It will shutdown if there is hardware issue(Ex: Ethernet being unplugged, or network card dead).
# @Author Carlos Avalos
Function Start-Monitoring
{

            $Shutdowndialog = new-object -comobject wscript.shell 
            $intAnswer = $Shutdowndialog.popup("ShutDown?",5,"Shutdown Prompt",4)
             if ($intAnswer -eq "6" ) { #Users can click yes or wait 5 seconds for the restart, or if doing maintence can stop the service by clicking cancel. 
                  Restart-Computer

                 }
             
              if($intAnswer -eq "7"){
                    Exit
                    }
          
            else{
                Restart-Computer

                }
          
        }
  
  Do {
           $nic = wmic Nic where "Name='Intel(R) 82579LM Gigabit Network Connection'" get "NetConnectionStatus"
           if($nic[2] -gt 7){
                   #Check
                   Start-Monitoring
            }
             if($nic[2] -eq 3){
                   Start-Monitoring
            }  
      }
      until($nic[2] -lt 2)

Start-Monitoring

    

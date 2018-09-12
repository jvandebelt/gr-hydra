#include "hydra/hydra_main.h"
#include "hydra/hydra_uhd_interface.h"

/* Configure the TX radio */
hydra::uhd_hydra_sptr usrp = std::make_shared<hydra::device_uhd>();

void
signal_handler(int signum)
{
  std::cout << "FODA-SE" << std::endl;
  usrp->release();
}


int main()
{
   signal(SIGINT, signal_handler);
   signal(SIGQUIT, signal_handler);
   signal(SIGABRT, signal_handler);
   signal(SIGHUP, signal_handler);

   /* TRANSMITTER */
   double d_tx_centre_freq = 950e6;
   double d_tx_samp_rate   = 2e6;
   unsigned int u_tx_fft_size = 1024;

   /* RECEIVER */
   double d_rx_centre_freq = 950e6;
   double d_rx_samp_rate   = 2e6;
   unsigned int u_rx_fft_size = 1024;

   /* Control port */
   unsigned int u_port = 5000;

   /* Instantiate XVL */
   hydra::HydraMain main = hydra::HydraMain(u_port);


   main.set_tx_config(
     usrp,
     d_tx_centre_freq,
     d_tx_samp_rate,
     u_tx_fft_size);

   main.set_rx_config(
     usrp,
     d_rx_centre_freq,
     d_rx_samp_rate,
     u_rx_fft_size);

   /* Run server */
   main.run();

   /* Run server */
   return 0;
}

#include "hydra/hydra_main.h"
#include "hydra/hydra_uhd_interface.h"

int main()
{
   // Transmitter
   // Centre frequency in Hz
   double d_tx_centre_freq = 2.0e9;
   // Sampling rate in mega samples per second
   double d_tx_samp_rate = 2e6;
   // FFT size
   unsigned int u_tx_fft_size = 1024;

   // Control port
   unsigned int u_port = 5000;

   // Instantiate XVL
   hydra::HydraMain main = hydra::HydraMain(u_port);

   // Configure the RX radio
   /*
     main.set_rx_config(d_rx_centre_freq,
     d_rx_samp_rate,
     u_rx_fft_size);
   */

   // Configure the TX radio
   hydra::uhd_hydra_sptr usrp = std::make_shared<hydra::device_uhd>();
   usrp->set_tx_config(d_tx_centre_freq, d_tx_samp_rate, 60.0);

   main.set_tx_config(
      usrp,
      d_tx_centre_freq,
      d_tx_samp_rate,
      u_tx_fft_size);

   // Run server
   main.run();

   // Run server
   return 0;
}

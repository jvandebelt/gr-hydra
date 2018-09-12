#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "hydra_gr_client_source_impl.h"

namespace gr {
  namespace hydra {

hydra_gr_client_source::sptr
hydra_gr_client_source::make(unsigned           u_id,
                             const std::string &host,
                             unsigned int       port)
{
  return gnuradio::get_initial_sptr(new hydra_gr_client_source_impl(u_id, host, port));
}

/* CTOR
 */
hydra_gr_client_source_impl::hydra_gr_client_source_impl(unsigned int u_id,
                                                         const std::string &s_host,
                                                         unsigned int u_port):
  gr::hier_block2("gr_client_source",
                  gr::io_signature::make(0, 0, 0),
                  gr::io_signature::make(1, 1, sizeof(gr_complex)))
{
  g_host = s_host;
  client = std::make_unique<hydra_client>(s_host, u_port, u_id, true);
  client->check_connection();
}

hydra_gr_client_source_impl::~hydra_gr_client_source_impl()
{
  client->free_resources();
}

bool
hydra_gr_client_source_impl::stop()
{
  client->free_resources();
}

void hydra_gr_client_source_impl::start_client(double d_center_frequency,
                                               double d_samp_rate,
                                               size_t u_payload)
{
  int i_rx_port = client->request_rx_resources(d_center_frequency, d_samp_rate, false);

  if (i_rx_port)
  {
    d_udp_source = gr::blocks::udp_source::make(sizeof(gr_complex),
                                                g_host,
                                                i_rx_port,
                                                u_payload,
                                                false);

    connect(d_udp_source, 0, self(), 0);
    std::cout << boost::format("Client Source initialized successfully: (%1%: %2%)") % g_host % i_rx_port << std::endl;
  }
  else
  {
    std::cerr << "Not able to reserve resources." << std::endl;
    exit(1);
  }
}

} /* namespace hydra */
} /* namespace gr */

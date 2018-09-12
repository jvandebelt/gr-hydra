#ifndef INCLUDED_HYDRA_GR_CLIENT_SOURCE_IMPL_H
#define INCLUDED_HYDRA_GR_CLIENT_SOURCE_IMPL_H

#include "hydra/hydra_gr_client_source.h"

#include <hydra/hydra_client.h>
#include <gnuradio/blocks/udp_source.h>


using namespace hydra;

namespace gr {
  namespace hydra {

class hydra_gr_client_source_impl : public hydra_gr_client_source
{
 public:
  /** CTOR
   */
  hydra_gr_client_source_impl(unsigned int u_id,
                              const std::string &host,
                              unsigned int u_port);

  /** DTOR
   */
  ~hydra_gr_client_source_impl();


  virtual void start_client(double d_center_frequency,
                            double d_samp_rate,
                            size_t u_payload);

  /**
   */
  virtual bool stop();

 private:
  gr::blocks::udp_source::sptr d_udp_source;
  std::unique_ptr<hydra_client> client;
  std::string g_host;
};

  } /* namespace hydra */
} /* namespace gr */

#endif /* INCLUDED_HYDRA_GR_CLIENT_SOURCE_IMPL_H */

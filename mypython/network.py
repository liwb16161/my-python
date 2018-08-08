import logging as LOG
import time 

class NetworkView():
    #list all network
    """
    List a new network.
    request header:HTTP_X_AUTH_TOKEN
    :return:
    """
    def check_token_id(fn):
        def fn_new(self,request,network_id):
            try:
               LOG.info("Try to get request headers")
               token_id = meta.get('HTTP_X_AUTH_TOKEN',None)
            except Exception as e:
                LOG.error("token_id is necessary!"+str(e))
                msg = "token_id is necessary!",e
                return common_error_response(msg,UNAUTHORIZED)
            fn(self,request,network_id)

        return fn_new



    @check_token_id
    def get(self,request, network_id):
        LOG.info("List all network")
        start_time = time.time()
        # meta = request.META
        # try:
        #     LOG.info("Try to get request headers")
        #     token_id = meta.get('HTTP_X_AUTH_TOKEN',None)
        # except Exception as e:
        #     LOG.error("token_id is necessary!"+str(e))
        #     msg = "token_id is necessary!",e
        #     return common_error_response(msg,UNAUTHORIZED)
        try:
            LOG.info("start to list network")
            networks = neutron_handler.list_networks(token_id)
            total_time = time.time() - start_time
            LOG.info("List network sucess! It cost %.3f"%total_time)
            return common_success_response(networks, RESPONSE_OK)
        except Exception as e:
            LOG.error('List network failed' + str(e))
            status_code = BADREQUEST
            msg = "List network failed! Error is:" + str(e)
            try:
                status_code = e.status_code
            except Exception as e:
                pass
            return common_error_response(msg,status_code)


    def post(self, request, network_id):
        """
        create a new network
        request header:HTTP_X_AUTH_TOKEN
        Request parameters are:
        {
          "network":{
          "name":"example_vpc",
          "shared":false,
          "provider:physical_network":"physnet2",
          "admin_state_up":true,
          "provider:network_type":"vlan",
          "router:external":false,
          "provider:segmentation_id":"2440"
           }
        }
        :param request:
        :return:
        """
        LOG.info("create a new network")
        start_time = time.time()
        meta = request.META
        try:
            LOG.info(" Get request headers ")
            token_id = meta.get('HTTP_X_AUTH_TOKEN', None)
        except Exception as e:
            msg = "token is empty"+str(e)
            return common_error_response(msg, error_code=UNAUTHORIZED)
        # get parameter
        # TODO:get necessery parameter
        try:
            name = request.data['network'].get('name')
            provider_physical_network = request.data['network'].get('provider:physical_network',None)
            admin_state_up = request.data.get('admin_state_up',None)
            if not admin_state_up:
                admin_state_up = 'true'
            provider_network_type = request.data.get('provider:network_type','vxlan')
            router_external = request.data.get('router:external',None)
            provider_segmentation_id = request.data.get('provider:segmentation_id',None)
            shared = request.data['network'].get('shared')
            if not shared:
                shared = 'false'
        except Exception as e:
            LOG.error("Get parameter failed! Error is" + str(e) )
            msg = 'Get parameter failed! Error is %s'%e
            return common_error_response(msg,BADREQUEST)
        #TODO:admin权限创建vlan
        kwargs = {}
        kwargs['name'] = name
        #kwargs['provider:physical_network'] = provider_physical_network
        #kwargs['provider:network_type'] = provider_network_type
        kwargs['admin_state_up'] = admin_state_up
        kwargs['shared'] = shared
        kwargs['router:external'] = router_external
        #kwargs['provider:segmentation_id'] = provider_segmentation_id
        try:
            LOG.info("start to create network")
            new_network = neutron_handler.create_network(token_id,**kwargs)
            total_time = time.time() - start_time
            LOG.info("Create network sucess! It cost %.3f" % total_time)
            return Response(new_network, RESPONSE_OK)
        except Exception as e:
            LOG.error("create network failed!error is" + str(e))
            msg = "create network failed! Error is:" + str(e)
            status_code = BADREQUEST
            try:
                status_code = e.status_code
            except Exception as e:
                pass
            return common_error_response(msg, status_code)
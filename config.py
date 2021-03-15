from os import environ

""" WIP """

class EnvironmentDetails:
    def __init__(self, base_url, test_data):
        self.base_url = base_url
        self.test_data = test_data


if "KUBERNETES_SERVICE_HOST" in environ:
    DEV = EnvironmentDetails(
        base_url="http://hermes-api",
        # test_data=testdata_dev,
    )
    STAGING = EnvironmentDetails(
        base_url="http://hermes-api",
        # test_data=testdata_staging,
    )
    PROD = EnvironmentDetails(
        base_url="http://hermes-api",
        # test_data=testdata_prod,

    )
else:
    DEV = EnvironmentDetails(
        base_url="https://web.dev.gb.bink.com/develop/wasabi/login",
        # test_data=testdata_dev,
    )
    STAGING = EnvironmentDetails(
        base_url="https://web.staging.gb.bink.com/develop/wasabi/login",
        # test_data=testdata_staging,
    )
    PROD = EnvironmentDetails(
        base_url="https://bink.com/wasabi",
        # test_data=testdata_prod,
    )


class ChannelDetails:
    def __init__(self, channel_name, bundle_id, client_id, organisation_id):
        self.channel_name = channel_name
        self.bundle_id = bundle_id
        self.client_id = client_id
        self.organisation_id = organisation_id


WASABI = ChannelDetails(
    channel_name="wasabi_ui",
    bundle_id="com.wasabi_ui.bink.web",
    client_id="KY6ia4AvWwl9GXnKfPMqHJy7U3vUE2pSpDjJaqazZ0LZCHu5dj",
    organisation_id="Wasabi",

)

BINK = ChannelDetails(
    channel_name="bink",
    bundle_id="com.bink.wallet",
    client_id="MKd3FfDGBi1CIUQwtahmPap64lneCa2R6GvVWKg6dNg4w9Jnpd",
    organisation_id="",
)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PreloadedUserSettings.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bPreloadedUserSettings.proto\x12\x35\x64iscord_protos.discord_users.v1.PreloadedUserSettings\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xabw\n\x15PreloadedUserSettings\x12l\n\x08versions\x18\x01 \x01(\x0b\x32U.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.VersionsH\x00\x88\x01\x01\x12n\n\x05inbox\x18\x02 \x01(\x0b\x32Z.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.InboxSettingsH\x01\x88\x01\x01\x12r\n\x06guilds\x18\x03 \x01(\x0b\x32].discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.AllGuildSettingsH\x02\x88\x01\x01\x12{\n\x0cuser_content\x18\x04 \x01(\x0b\x32`.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.UserContentSettingsH\x03\x88\x01\x01\x12\x80\x01\n\x0fvoice_and_video\x18\x05 \x01(\x0b\x32\x62.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.VoiceAndVideoSettingsH\x04\x88\x01\x01\x12\x80\x01\n\x0ftext_and_images\x18\x06 \x01(\x0b\x32\x62.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.TextAndImagesSettingsH\x05\x88\x01\x01\x12}\n\rnotifications\x18\x07 \x01(\x0b\x32\x61.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.NotificationSettingsH\x06\x88\x01\x01\x12r\n\x07privacy\x18\x08 \x01(\x0b\x32\\.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.PrivacySettingsH\x07\x88\x01\x01\x12n\n\x05\x64\x65\x62ug\x18\t \x01(\x0b\x32Z.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.DebugSettingsH\x08\x88\x01\x01\x12{\n\x0cgame_library\x18\n \x01(\x0b\x32`.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.GameLibrarySettingsH\t\x88\x01\x01\x12p\n\x06status\x18\x0b \x01(\x0b\x32[.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.StatusSettingsH\n\x88\x01\x01\x12|\n\x0clocalization\x18\x0c \x01(\x0b\x32\x61.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.LocalizationSettingsH\x0b\x88\x01\x01\x12x\n\nappearance\x18\r \x01(\x0b\x32_.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.AppearanceSettingsH\x0c\x88\x01\x01\x12u\n\rguild_folders\x18\x0e \x01(\x0b\x32Y.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.GuildFoldersH\r\x88\x01\x01\x12n\n\tfavorites\x18\x0f \x01(\x0b\x32V.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.FavoritesH\x0e\x88\x01\x01\x12\x7f\n\x16\x61udio_context_settings\x18\x10 \x01(\x0b\x32Z.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.AudioSettingsH\x0f\x88\x01\x01\x12z\n\x0b\x63ommunities\x18\x11 \x01(\x0b\x32`.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.CommunitiesSettingsH\x10\x88\x01\x01\x12v\n\tbroadcast\x18\x12 \x01(\x0b\x32^.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.BroadcastSettingsH\x11\x88\x01\x01\x12n\n\x05\x63lips\x18\x13 \x01(\x0b\x32Z.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.ClipsSettingsH\x12\x88\x01\x01\x1aP\n\x08Versions\x12\x16\n\x0e\x63lient_version\x18\x01 \x01(\r\x12\x16\n\x0eserver_version\x18\x02 \x01(\r\x12\x14\n\x0c\x64\x61ta_version\x18\x03 \x01(\r\x1a\x94\x01\n\rInboxSettings\x12j\n\x0b\x63urrent_tab\x18\x01 \x01(\x0e\x32U.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.InboxTab\x12\x17\n\x0fviewed_tutorial\x18\x02 \x01(\x08\x1a\xbe\x01\n\x10\x43hannelIconEmoji\x12-\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueH\x00\x88\x01\x01\x12/\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x01\x88\x01\x01\x12\x30\n\x05\x63olor\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueH\x02\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_nameB\x08\n\x06_color\x1a\xb4\x01\n\x0f\x43hannelSettings\x12\x1a\n\x12\x63ollapsed_in_inbox\x18\x01 \x01(\x08\x12v\n\nicon_emoji\x18\x02 \x01(\x0b\x32].discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.ChannelIconEmojiH\x00\x88\x01\x01\x42\r\n\x0b_icon_emoji\x1a\x35\n\x0f\x43ustomCallSound\x12\x10\n\x08sound_id\x18\x01 \x01(\x06\x12\x10\n\x08guild_id\x18\x02 \x01(\x06\x1a\xa5\x01\n\x13\x43hannelListSettings\x12\x31\n\x06layout\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x88\x01\x01\x12;\n\x10message_previews\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x01\x88\x01\x01\x42\t\n\x07_layoutB\x13\n\x11_message_previews\x1a\xe1\x06\n\rGuildSettings\x12z\n\x08\x63hannels\x18\x01 \x03(\x0b\x32h.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.GuildSettings.ChannelsEntry\x12\x14\n\x0chub_progress\x18\x02 \x01(\r\x12!\n\x19guild_onboarding_progress\x18\x03 \x01(\r\x12\x43\n\x1aguild_recents_dismissed_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x12\x1f\n\x17\x64ismissed_guild_content\x18\x05 \x01(\x0c\x12u\n\njoin_sound\x18\x06 \x01(\x0b\x32\\.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.CustomCallSoundH\x01\x88\x01\x01\x12\x94\x01\n%mobile_redesign_channel_list_settings\x18\x07 \x01(\x0b\x32`.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.ChannelListSettingsH\x02\x88\x01\x01\x12\x1f\n\x17\x64isable_raid_alert_push\x18\x08 \x01(\x08\x12\x1e\n\x16\x64isable_raid_alert_nag\x18\t \x01(\x08\x1a\x8d\x01\n\rChannelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12k\n\x05value\x18\x02 \x01(\x0b\x32\\.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.ChannelSettings:\x02\x38\x01\x42\x1d\n\x1b_guild_recents_dismissed_atB\r\n\x0b_join_soundB(\n&_mobile_redesign_channel_list_settings\x1a\x99\x02\n\x10\x41llGuildSettings\x12y\n\x06guilds\x18\x01 \x03(\x0b\x32i.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.AllGuildSettings.GuildsEntry\x1a\x89\x01\n\x0bGuildsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12i\n\x05value\x18\x02 \x01(\x0b\x32Z.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.GuildSettings:\x02\x38\x01\x1a\xa7\x04\n\x13UserContentSettings\x12\x1a\n\x12\x64ismissed_contents\x18\x01 \x01(\x0c\x12W\n,last_dismissed_outbound_promotion_start_date\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x88\x01\x01\x12J\n!premium_tier_0_modal_dismissed_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x88\x01\x01\x12M\n$guild_onboarding_upsell_dismissed_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x02\x88\x01\x01\x12R\n)safety_user_sentiment_notice_dismissed_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x03\x88\x01\x01\x42/\n-_last_dismissed_outbound_promotion_start_dateB$\n\"_premium_tier_0_modal_dismissed_atB\'\n%_guild_onboarding_upsell_dismissed_atB,\n*_safety_user_sentiment_notice_dismissed_at\x1a-\n\x19VideoFilterBackgroundBlur\x12\x10\n\x08use_blur\x18\x01 \x01(\x08\x1a\x32\n\x10VideoFilterAsset\x12\n\n\x02id\x18\x01 \x01(\x06\x12\x12\n\nasset_hash\x18\x02 \x01(\t\x1a$\n\x12SoundboardSettings\x12\x0e\n\x06volume\x18\x01 \x01(\x02\x1a\xad\x06\n\x15VoiceAndVideoSettings\x12t\n\x04\x62lur\x18\x01 \x01(\x0b\x32\x66.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.VideoFilterBackgroundBlur\x12\x15\n\rpreset_option\x18\x02 \x01(\r\x12s\n\x0c\x63ustom_asset\x18\x03 \x01(\x0b\x32].discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.VideoFilterAsset\x12=\n\x14\x61lways_preview_video\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x00\x88\x01\x01\x12\x36\n\x0b\x61\x66k_timeout\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueH\x01\x88\x01\x01\x12\x45\n\x1cstream_notifications_enabled\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x02\x88\x01\x01\x12I\n native_phone_integration_enabled\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x03\x88\x01\x01\x12\x81\x01\n\x13soundboard_settings\x18\t \x01(\x0b\x32_.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.SoundboardSettingsH\x04\x88\x01\x01\x42\x17\n\x15_always_preview_videoB\x0e\n\x0c_afk_timeoutB\x1f\n\x1d_stream_notifications_enabledB#\n!_native_phone_integration_enabledB\x16\n\x14_soundboard_settings\x1a\xbe\x03\n\x17\x45xplicitContentSettings\x12\x86\x01\n\x17\x65xplicit_content_guilds\x18\x01 \x01(\x0e\x32\x65.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.ExplicitContentRedaction\x12\x89\x01\n\x1a\x65xplicit_content_friend_dm\x18\x02 \x01(\x0e\x32\x65.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.ExplicitContentRedaction\x12\x8d\x01\n\x1e\x65xplicit_content_non_friend_dm\x18\x03 \x01(\x0e\x32\x65.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.ExplicitContentRedaction\x1a\x8c\x13\n\x15TextAndImagesSettings\x12>\n\x13\x64iversity_surrogate\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x88\x01\x01\x12<\n\x13use_rich_chat_input\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x01\x88\x01\x01\x12;\n\x12use_thread_sidebar\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x02\x88\x01\x01\x12:\n\x0frender_spoilers\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x03\x88\x01\x01\x12\'\n\x1f\x65moji_picker_collapsed_sections\x18\x05 \x03(\t\x12)\n!sticker_picker_collapsed_sections\x18\x06 \x03(\t\x12@\n\x17view_image_descriptions\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x04\x88\x01\x01\x12\x41\n\x18show_command_suggestions\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x05\x88\x01\x01\x12@\n\x17inline_attachment_media\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x06\x88\x01\x01\x12;\n\x12inline_embed_media\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x07\x88\x01\x01\x12\x36\n\rgif_auto_play\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x08\x88\x01\x01\x12\x36\n\rrender_embeds\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\t\x88\x01\x01\x12\x39\n\x10render_reactions\x18\r \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\n\x88\x01\x01\x12\x36\n\ranimate_emoji\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x0b\x88\x01\x01\x12;\n\x10\x61nimate_stickers\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueH\x0c\x88\x01\x01\x12;\n\x12\x65nable_tts_command\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\r\x88\x01\x01\x12@\n\x17message_display_compact\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x0e\x88\x01\x01\x12\x42\n\x17\x65xplicit_content_filter\x18\x13 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueH\x0f\x88\x01\x01\x12\x39\n\x10view_nsfw_guilds\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x10\x88\x01\x01\x12:\n\x11\x63onvert_emoticons\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x11\x88\x01\x01\x12G\n\x1e\x65xpression_suggestions_enabled\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x12\x88\x01\x01\x12;\n\x12view_nsfw_commands\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x13\x88\x01\x01\x12>\n\x15use_legacy_chat_input\x18\x18 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x14\x88\x01\x01\x12,\n$soundboard_picker_collapsed_sections\x18\x19 \x03(\t\x12\x39\n\x0e\x64m_spam_filter\x18\x1a \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueH\x15\x88\x01\x01\x12v\n\x11\x64m_spam_filter_v2\x18\x1b \x01(\x0e\x32[.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.DmSpamFilterV2\x12I\n include_stickers_in_autocomplete\x18\x1c \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x16\x88\x01\x01\x12\x8c\x01\n\x19\x65xplicit_content_settings\x18\x1d \x01(\x0b\x32\x64.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.ExplicitContentSettingsH\x17\x88\x01\x01\x42\x16\n\x14_diversity_surrogateB\x16\n\x14_use_rich_chat_inputB\x15\n\x13_use_thread_sidebarB\x12\n\x10_render_spoilersB\x1a\n\x18_view_image_descriptionsB\x1b\n\x19_show_command_suggestionsB\x1a\n\x18_inline_attachment_mediaB\x15\n\x13_inline_embed_mediaB\x10\n\x0e_gif_auto_playB\x10\n\x0e_render_embedsB\x13\n\x11_render_reactionsB\x10\n\x0e_animate_emojiB\x13\n\x11_animate_stickersB\x15\n\x13_enable_tts_commandB\x1a\n\x18_message_display_compactB\x1a\n\x18_explicit_content_filterB\x13\n\x11_view_nsfw_guildsB\x14\n\x12_convert_emoticonsB!\n\x1f_expression_suggestions_enabledB\x15\n\x13_view_nsfw_commandsB\x18\n\x16_use_legacy_chat_inputB\x11\n\x0f_dm_spam_filterB#\n!_include_stickers_in_autocompleteB\x1c\n\x1a_explicit_content_settings\x1a\xfd\x02\n\x14NotificationSettings\x12\x42\n\x19show_in_app_notifications\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x00\x88\x01\x01\x12\x42\n\x19notify_friends_on_go_live\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x01\x88\x01\x01\x12+\n#notification_center_acked_before_id\x18\x03 \x01(\x06\x12L\n#enable_burst_reaction_notifications\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x02\x88\x01\x01\x42\x1c\n\x1a_show_in_app_notificationsB\x1c\n\x1a_notify_friends_on_go_liveB&\n$_enable_burst_reaction_notifications\x1a\x88\r\n\x0fPrivacySettings\x12M\n$allow_activity_party_privacy_friends\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x00\x88\x01\x01\x12S\n*allow_activity_party_privacy_voice_channel\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x01\x88\x01\x01\x12\x1c\n\x14restricted_guild_ids\x18\x03 \x03(\x06\x12!\n\x19\x64\x65\x66\x61ult_guilds_restricted\x18\x04 \x01(\x08\x12%\n\x1d\x61llow_accessibility_detection\x18\x07 \x01(\x08\x12\x41\n\x18\x64\x65tect_platform_accounts\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x02\x88\x01\x01\x12\x35\n\x0cpasswordless\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x03\x88\x01\x01\x12=\n\x14\x63ontact_sync_enabled\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x04\x88\x01\x01\x12>\n\x13\x66riend_source_flags\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueH\x05\x88\x01\x01\x12\x41\n\x16\x66riend_discovery_flags\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueH\x06\x88\x01\x01\x12%\n\x1d\x61\x63tivity_restricted_guild_ids\x18\r \x03(\x06\x12\x9e\x01\n\"default_guilds_activity_restricted\x18\x0e \x01(\x0e\x32r.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.GuildActivityStatusRestrictionDefault\x12-\n%activity_joining_restricted_guild_ids\x18\x0f \x03(\x06\x12,\n$message_request_restricted_guild_ids\x18\x10 \x03(\x06\x12K\n\"default_message_request_restricted\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x07\x88\x01\x01\x12\x38\n\x0f\x64rops_opted_out\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x08\x88\x01\x01\x12\x43\n\x1anon_spam_retraining_opt_in\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\t\x88\x01\x01\x12>\n\x15\x66\x61mily_center_enabled\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\n\x88\x01\x01\x12\x41\n\x18\x66\x61mily_center_enabled_v2\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x0b\x88\x01\x01\x12=\n\x14hide_legacy_username\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x0c\x88\x01\x01\x42\'\n%_allow_activity_party_privacy_friendsB-\n+_allow_activity_party_privacy_voice_channelB\x1b\n\x19_detect_platform_accountsB\x0f\n\r_passwordlessB\x17\n\x15_contact_sync_enabledB\x16\n\x14_friend_source_flagsB\x19\n\x17_friend_discovery_flagsB%\n#_default_message_request_restrictedB\x12\n\x10_drops_opted_outB\x1d\n\x1b_non_spam_retraining_opt_inB\x18\n\x16_family_center_enabledB\x1b\n\x19_family_center_enabled_v2B\x17\n\x15_hide_legacy_username\x1au\n\rDebugSettings\x12\x44\n\x1brtc_panel_show_voice_states\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x00\x88\x01\x01\x42\x1e\n\x1c_rtc_panel_show_voice_states\x1a\xad\x02\n\x13GameLibrarySettings\x12\x41\n\x18install_shortcut_desktop\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x00\x88\x01\x01\x12\x44\n\x1binstall_shortcut_start_menu\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x01\x88\x01\x01\x12:\n\x11\x64isable_games_tab\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x02\x88\x01\x01\x42\x1b\n\x19_install_shortcut_desktopB\x1e\n\x1c_install_shortcut_start_menuB\x14\n\x12_disable_games_tab\x1aY\n\x0c\x43ustomStatus\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x08\x65moji_id\x18\x02 \x01(\x06\x12\x12\n\nemoji_name\x18\x03 \x01(\t\x12\x15\n\rexpires_at_ms\x18\x04 \x01(\x06\x1a\xa9\x02\n\x0eStatusSettings\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x88\x01\x01\x12u\n\rcustom_status\x18\x02 \x01(\x0b\x32Y.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.CustomStatusH\x01\x88\x01\x01\x12:\n\x11show_current_game\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x02\x88\x01\x01\x42\t\n\x07_statusB\x10\n\x0e_custom_statusB\x14\n\x12_show_current_game\x1a\xa3\x01\n\x14LocalizationSettings\x12\x31\n\x06locale\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x88\x01\x01\x12\x39\n\x0ftimezone_offset\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueH\x01\x88\x01\x01\x42\t\n\x07_localeB\x12\n\x10_timezone_offset\x1a\xb0\x02\n\x13\x43lientThemeSettings\x12\x38\n\rprimary_color\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueH\x00\x88\x01\x01\x12H\n\x1d\x62\x61\x63kground_gradient_preset_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueH\x01\x88\x01\x01\x12\x43\n\x19\x62\x61\x63kground_gradient_angle\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValueH\x02\x88\x01\x01\x42\x10\n\x0e_primary_colorB \n\x1e_background_gradient_preset_idB\x1c\n\x1a_background_gradient_angle\x1a\xfc\x03\n\x12\x41ppearanceSettings\x12\x61\n\x05theme\x18\x01 \x01(\x0e\x32R.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.Theme\x12\x16\n\x0e\x64\x65veloper_mode\x18\x02 \x01(\x08\x12\x84\x01\n\x15\x63lient_theme_settings\x18\x03 \x01(\x0b\x32`.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.ClientThemeSettingsH\x00\x88\x01\x01\x12 \n\x18mobile_redesign_disabled\x18\x04 \x01(\x08\x12>\n\x13\x63hannel_list_layout\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x01\x88\x01\x01\x12;\n\x10message_previews\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x02\x88\x01\x01\x42\x18\n\x16_client_theme_settingsB\x16\n\x14_channel_list_layoutB\x13\n\x11_message_previews\x1a\xcb\x01\n\x0bGuildFolder\x12\x11\n\tguild_ids\x18\x01 \x03(\x06\x12,\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueH\x00\x88\x01\x01\x12/\n\x04name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x01\x88\x01\x01\x12\x30\n\x05\x63olor\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueH\x02\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_nameB\x08\n\x06_color\x1a\x92\x01\n\x0cGuildFolders\x12i\n\x07\x66olders\x18\x01 \x03(\x0b\x32X.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.GuildFolder\x12\x17\n\x0fguild_positions\x18\x02 \x03(\x06\x1a\xb8\x01\n\x0f\x46\x61voriteChannel\x12\x10\n\x08nickname\x18\x01 \x01(\t\x12n\n\x04type\x18\x02 \x01(\x0e\x32`.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.FavoriteChannelType\x12\x10\n\x08position\x18\x03 \x01(\r\x12\x11\n\tparent_id\x18\x04 \x01(\x06\x1a\xbc\x02\n\tFavorites\x12\x87\x01\n\x11\x66\x61vorite_channels\x18\x01 \x03(\x0b\x32l.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.Favorites.FavoriteChannelsEntry\x12\r\n\x05muted\x18\x02 \x01(\x08\x1a\x95\x01\n\x15\x46\x61voriteChannelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12k\n\x05value\x18\x02 \x01(\x0b\x32\\.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.FavoriteChannel:\x02\x38\x01\x1a\x63\n\x13\x41udioContextSetting\x12\r\n\x05muted\x18\x01 \x01(\x08\x12\x0e\n\x06volume\x18\x02 \x01(\x02\x12\x13\n\x0bmodified_at\x18\x03 \x01(\x06\x12\x18\n\x10soundboard_muted\x18\x04 \x01(\x08\x1a\x9d\x04\n\rAudioSettings\x12r\n\x04user\x18\x01 \x03(\x0b\x32\x64.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.AudioSettings.UserEntry\x12v\n\x06stream\x18\x02 \x03(\x0b\x32\x66.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.AudioSettings.StreamEntry\x1a\x8d\x01\n\tUserEntry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12o\n\x05value\x18\x02 \x01(\x0b\x32`.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.AudioContextSetting:\x02\x38\x01\x1a\x8f\x01\n\x0bStreamEntry\x12\x0b\n\x03key\x18\x01 \x01(\x06\x12o\n\x05value\x18\x02 \x01(\x0b\x32`.discord_protos.discord_users.v1.PreloadedUserSettings.PreloadedUserSettings.AudioContextSetting:\x02\x38\x01\x1ao\n\x13\x43ommunitiesSettings\x12>\n\x15\x64isable_home_auto_nav\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x00\x88\x01\x01\x42\x18\n\x16_disable_home_auto_nav\x1a\xde\x01\n\x11\x42roadcastSettings\x12\x36\n\rallow_friends\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x00\x88\x01\x01\x12\x19\n\x11\x61llowed_guild_ids\x18\x02 \x03(\x06\x12\x18\n\x10\x61llowed_user_ids\x18\x03 \x03(\x06\x12\x37\n\x0e\x61uto_broadcast\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x01\x88\x01\x01\x42\x10\n\x0e_allow_friendsB\x11\n\x0f_auto_broadcast\x1ai\n\rClipsSettings\x12>\n\x15\x61llow_voice_recording\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x00\x88\x01\x01\x42\x18\n\x16_allow_voice_recording\"N\n\x08InboxTab\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0c\n\x08MENTIONS\x10\x01\x12\x0b\n\x07UNREADS\x10\x02\x12\t\n\x05TODOS\x10\x03\x12\x0b\n\x07\x46OR_YOU\x10\x04\"_\n\x0e\x44mSpamFilterV2\x12\x11\n\rDEFAULT_UNSET\x10\x00\x12\x0c\n\x08\x44ISABLED\x10\x01\x12\x0f\n\x0bNON_FRIENDS\x10\x02\x12\x1b\n\x17\x46RIENDS_AND_NON_FRIENDS\x10\x03\"_\n\x18\x45xplicitContentRedaction\x12$\n UNSET_EXPLICIT_CONTENT_REDACTION\x10\x00\x12\x08\n\x04SHOW\x10\x01\x12\x08\n\x04\x42LUR\x10\x02\x12\t\n\x05\x42LOCK\x10\x03\"I\n%GuildActivityStatusRestrictionDefault\x12\x07\n\x03OFF\x10\x00\x12\x17\n\x13ON_FOR_LARGE_GUILDS\x10\x01\"\'\n\x05Theme\x12\t\n\x05UNSET\x10\x00\x12\x08\n\x04\x44\x41RK\x10\x01\x12\t\n\x05LIGHT\x10\x02\"\\\n\x13\x46\x61voriteChannelType\x12\x1f\n\x1bUNSET_FAVORITE_CHANNEL_TYPE\x10\x00\x12\x16\n\x12REFERENCE_ORIGINAL\x10\x01\x12\x0c\n\x08\x43\x41TEGORY\x10\x02\x42\x0b\n\t_versionsB\x08\n\x06_inboxB\t\n\x07_guildsB\x0f\n\r_user_contentB\x12\n\x10_voice_and_videoB\x12\n\x10_text_and_imagesB\x10\n\x0e_notificationsB\n\n\x08_privacyB\x08\n\x06_debugB\x0f\n\r_game_libraryB\t\n\x07_statusB\x0f\n\r_localizationB\r\n\x0b_appearanceB\x10\n\x0e_guild_foldersB\x0c\n\n_favoritesB\x19\n\x17_audio_context_settingsB\x0e\n\x0c_communitiesB\x0c\n\n_broadcastB\x08\n\x06_clipsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PreloadedUserSettings_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRELOADEDUSERSETTINGS_GUILDSETTINGS_CHANNELSENTRY._options = None
  _PRELOADEDUSERSETTINGS_GUILDSETTINGS_CHANNELSENTRY._serialized_options = b'8\001'
  _PRELOADEDUSERSETTINGS_ALLGUILDSETTINGS_GUILDSENTRY._options = None
  _PRELOADEDUSERSETTINGS_ALLGUILDSETTINGS_GUILDSENTRY._serialized_options = b'8\001'
  _PRELOADEDUSERSETTINGS_FAVORITES_FAVORITECHANNELSENTRY._options = None
  _PRELOADEDUSERSETTINGS_FAVORITES_FAVORITECHANNELSENTRY._serialized_options = b'8\001'
  _PRELOADEDUSERSETTINGS_AUDIOSETTINGS_USERENTRY._options = None
  _PRELOADEDUSERSETTINGS_AUDIOSETTINGS_USERENTRY._serialized_options = b'8\001'
  _PRELOADEDUSERSETTINGS_AUDIOSETTINGS_STREAMENTRY._options = None
  _PRELOADEDUSERSETTINGS_AUDIOSETTINGS_STREAMENTRY._serialized_options = b'8\001'
  _PRELOADEDUSERSETTINGS._serialized_start=152
  _PRELOADEDUSERSETTINGS._serialized_end=15427
  _PRELOADEDUSERSETTINGS_VERSIONS._serialized_start=2460
  _PRELOADEDUSERSETTINGS_VERSIONS._serialized_end=2540
  _PRELOADEDUSERSETTINGS_INBOXSETTINGS._serialized_start=2543
  _PRELOADEDUSERSETTINGS_INBOXSETTINGS._serialized_end=2691
  _PRELOADEDUSERSETTINGS_CHANNELICONEMOJI._serialized_start=2694
  _PRELOADEDUSERSETTINGS_CHANNELICONEMOJI._serialized_end=2884
  _PRELOADEDUSERSETTINGS_CHANNELSETTINGS._serialized_start=2887
  _PRELOADEDUSERSETTINGS_CHANNELSETTINGS._serialized_end=3067
  _PRELOADEDUSERSETTINGS_CUSTOMCALLSOUND._serialized_start=3069
  _PRELOADEDUSERSETTINGS_CUSTOMCALLSOUND._serialized_end=3122
  _PRELOADEDUSERSETTINGS_CHANNELLISTSETTINGS._serialized_start=3125
  _PRELOADEDUSERSETTINGS_CHANNELLISTSETTINGS._serialized_end=3290
  _PRELOADEDUSERSETTINGS_GUILDSETTINGS._serialized_start=3293
  _PRELOADEDUSERSETTINGS_GUILDSETTINGS._serialized_end=4158
  _PRELOADEDUSERSETTINGS_GUILDSETTINGS_CHANNELSENTRY._serialized_start=3929
  _PRELOADEDUSERSETTINGS_GUILDSETTINGS_CHANNELSENTRY._serialized_end=4070
  _PRELOADEDUSERSETTINGS_ALLGUILDSETTINGS._serialized_start=4161
  _PRELOADEDUSERSETTINGS_ALLGUILDSETTINGS._serialized_end=4442
  _PRELOADEDUSERSETTINGS_ALLGUILDSETTINGS_GUILDSENTRY._serialized_start=4305
  _PRELOADEDUSERSETTINGS_ALLGUILDSETTINGS_GUILDSENTRY._serialized_end=4442
  _PRELOADEDUSERSETTINGS_USERCONTENTSETTINGS._serialized_start=4445
  _PRELOADEDUSERSETTINGS_USERCONTENTSETTINGS._serialized_end=4996
  _PRELOADEDUSERSETTINGS_VIDEOFILTERBACKGROUNDBLUR._serialized_start=4998
  _PRELOADEDUSERSETTINGS_VIDEOFILTERBACKGROUNDBLUR._serialized_end=5043
  _PRELOADEDUSERSETTINGS_VIDEOFILTERASSET._serialized_start=5045
  _PRELOADEDUSERSETTINGS_VIDEOFILTERASSET._serialized_end=5095
  _PRELOADEDUSERSETTINGS_SOUNDBOARDSETTINGS._serialized_start=5097
  _PRELOADEDUSERSETTINGS_SOUNDBOARDSETTINGS._serialized_end=5133
  _PRELOADEDUSERSETTINGS_VOICEANDVIDEOSETTINGS._serialized_start=5136
  _PRELOADEDUSERSETTINGS_VOICEANDVIDEOSETTINGS._serialized_end=5949
  _PRELOADEDUSERSETTINGS_EXPLICITCONTENTSETTINGS._serialized_start=5952
  _PRELOADEDUSERSETTINGS_EXPLICITCONTENTSETTINGS._serialized_end=6398
  _PRELOADEDUSERSETTINGS_TEXTANDIMAGESSETTINGS._serialized_start=6401
  _PRELOADEDUSERSETTINGS_TEXTANDIMAGESSETTINGS._serialized_end=8845
  _PRELOADEDUSERSETTINGS_NOTIFICATIONSETTINGS._serialized_start=8848
  _PRELOADEDUSERSETTINGS_NOTIFICATIONSETTINGS._serialized_end=9229
  _PRELOADEDUSERSETTINGS_PRIVACYSETTINGS._serialized_start=9232
  _PRELOADEDUSERSETTINGS_PRIVACYSETTINGS._serialized_end=10904
  _PRELOADEDUSERSETTINGS_DEBUGSETTINGS._serialized_start=10906
  _PRELOADEDUSERSETTINGS_DEBUGSETTINGS._serialized_end=11023
  _PRELOADEDUSERSETTINGS_GAMELIBRARYSETTINGS._serialized_start=11026
  _PRELOADEDUSERSETTINGS_GAMELIBRARYSETTINGS._serialized_end=11327
  _PRELOADEDUSERSETTINGS_CUSTOMSTATUS._serialized_start=11329
  _PRELOADEDUSERSETTINGS_CUSTOMSTATUS._serialized_end=11418
  _PRELOADEDUSERSETTINGS_STATUSSETTINGS._serialized_start=11421
  _PRELOADEDUSERSETTINGS_STATUSSETTINGS._serialized_end=11718
  _PRELOADEDUSERSETTINGS_LOCALIZATIONSETTINGS._serialized_start=11721
  _PRELOADEDUSERSETTINGS_LOCALIZATIONSETTINGS._serialized_end=11884
  _PRELOADEDUSERSETTINGS_CLIENTTHEMESETTINGS._serialized_start=11887
  _PRELOADEDUSERSETTINGS_CLIENTTHEMESETTINGS._serialized_end=12191
  _PRELOADEDUSERSETTINGS_APPEARANCESETTINGS._serialized_start=12194
  _PRELOADEDUSERSETTINGS_APPEARANCESETTINGS._serialized_end=12702
  _PRELOADEDUSERSETTINGS_GUILDFOLDER._serialized_start=12705
  _PRELOADEDUSERSETTINGS_GUILDFOLDER._serialized_end=12908
  _PRELOADEDUSERSETTINGS_GUILDFOLDERS._serialized_start=12911
  _PRELOADEDUSERSETTINGS_GUILDFOLDERS._serialized_end=13057
  _PRELOADEDUSERSETTINGS_FAVORITECHANNEL._serialized_start=13060
  _PRELOADEDUSERSETTINGS_FAVORITECHANNEL._serialized_end=13244
  _PRELOADEDUSERSETTINGS_FAVORITES._serialized_start=13247
  _PRELOADEDUSERSETTINGS_FAVORITES._serialized_end=13563
  _PRELOADEDUSERSETTINGS_FAVORITES_FAVORITECHANNELSENTRY._serialized_start=13414
  _PRELOADEDUSERSETTINGS_FAVORITES_FAVORITECHANNELSENTRY._serialized_end=13563
  _PRELOADEDUSERSETTINGS_AUDIOCONTEXTSETTING._serialized_start=13565
  _PRELOADEDUSERSETTINGS_AUDIOCONTEXTSETTING._serialized_end=13664
  _PRELOADEDUSERSETTINGS_AUDIOSETTINGS._serialized_start=13667
  _PRELOADEDUSERSETTINGS_AUDIOSETTINGS._serialized_end=14208
  _PRELOADEDUSERSETTINGS_AUDIOSETTINGS_USERENTRY._serialized_start=13921
  _PRELOADEDUSERSETTINGS_AUDIOSETTINGS_USERENTRY._serialized_end=14062
  _PRELOADEDUSERSETTINGS_AUDIOSETTINGS_STREAMENTRY._serialized_start=14065
  _PRELOADEDUSERSETTINGS_AUDIOSETTINGS_STREAMENTRY._serialized_end=14208
  _PRELOADEDUSERSETTINGS_COMMUNITIESSETTINGS._serialized_start=14210
  _PRELOADEDUSERSETTINGS_COMMUNITIESSETTINGS._serialized_end=14321
  _PRELOADEDUSERSETTINGS_BROADCASTSETTINGS._serialized_start=14324
  _PRELOADEDUSERSETTINGS_BROADCASTSETTINGS._serialized_end=14546
  _PRELOADEDUSERSETTINGS_CLIPSSETTINGS._serialized_start=14548
  _PRELOADEDUSERSETTINGS_CLIPSSETTINGS._serialized_end=14653
  _PRELOADEDUSERSETTINGS_INBOXTAB._serialized_start=14655
  _PRELOADEDUSERSETTINGS_INBOXTAB._serialized_end=14733
  _PRELOADEDUSERSETTINGS_DMSPAMFILTERV2._serialized_start=14735
  _PRELOADEDUSERSETTINGS_DMSPAMFILTERV2._serialized_end=14830
  _PRELOADEDUSERSETTINGS_EXPLICITCONTENTREDACTION._serialized_start=14832
  _PRELOADEDUSERSETTINGS_EXPLICITCONTENTREDACTION._serialized_end=14927
  _PRELOADEDUSERSETTINGS_GUILDACTIVITYSTATUSRESTRICTIONDEFAULT._serialized_start=14929
  _PRELOADEDUSERSETTINGS_GUILDACTIVITYSTATUSRESTRICTIONDEFAULT._serialized_end=15002
  _PRELOADEDUSERSETTINGS_THEME._serialized_start=15004
  _PRELOADEDUSERSETTINGS_THEME._serialized_end=15043
  _PRELOADEDUSERSETTINGS_FAVORITECHANNELTYPE._serialized_start=15045
  _PRELOADEDUSERSETTINGS_FAVORITECHANNELTYPE._serialized_end=15137
# @@protoc_insertion_point(module_scope)

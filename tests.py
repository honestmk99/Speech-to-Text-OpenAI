from speechgpt import SpeechGPT

session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..odXrMgmSl84Oqew4.Rnja0U6jspu-hbon3PvNgRO5Q3GP8wM0LRkHEHOIoGU3OquWzTC9aiaL-UCmnO0nnSsGzitPDOGT2_6ySzSU_M4lZKpxTlkL_SG-NrqMnWD7ktl2gIoosMVAQ7dhroVoemfzy7CAMwk4MRk4eKpV4HUzhkgB-PPxHJbQlilEctJ3cPQCaA0v-2oHvl2gn_GTCglWo4PVzZZzfOkh1M-sw8fxl03bG665vYYvrFk2XA5cdqYC2AJ2h9M85Qc5aCkWi6_YyST_iF3JvyEiL149QGEaFPxFg7BfPRWh74XR2utlvGsQ6iev0Lo9_TOH1ySDBGw0M2vDAxUcQbHDj0rQysiTi6zq9XyGGKyS3Lsota5h0Q-Gw6nX2Tj-grFoKE_sc0tic3i6aF74GJ-7ZvjHiU1tzLI5Nz2vxoT4WMjJP8ZDHtdeLxhS-MmX_v2IRRpEeKNK7r79yCBc-ENaGNCfKjC0RYAstd2f4KaPlhtcuIsX3z9gsDAvPvhRdpIs3f2uIx7nJDpxMPACsLkxja_woSwx8burnGYqTtBpz89h_xcY5UyaXLtRExzs8T2i14HZwHLLj-gkpVuy3YBvqqREgyPW5OnEKV-4DXwr7Ynjf7x_9bRg3NbaiDtxSJvy8dTtx3gyUrogAD3q-YosrSkcpGe9iCDudmeqocF-TPWtTQPSYwYRS9N-IT-7scT6X4wNtbYkYUYHKnN_ww4NQwZ7NYACQy5Ayg2_2S64lwG7VwTtYjW3plNZfhQ68qcbXRk-UJaS_WrsIclUfFCSgRJyn9MMyI00OfkXPd7pSRw1pGht2ZJy2pZlbZqkR1M9eC6jxgwOA5-c2j2iGbbLecf07WYuNuHtBLYGntxHK_f7PwxvrKSbrWKqc9qYDzSOPt4PMXGPKgKzgq1LvrNbjDTX5lUvyf5ff6n5nYR8u_qCZimgG3Uo7EKTjZBYDIyo976VSliJ7U_gft1nJjtV4ulY3gsDd-_QA2Q4H_eGWhFJ5xZvof3IuaxF0FZdbDdgsEYg15wW9r6J3nS-LW0ICyTlZ0U_xxlsAXgncZBvNoC9UD8fy9gUPxipjJaol4AbG3-YIDT5dqutHwj0C5xqXIPTlQ973UElod4U6KlBI9DJHIuDuS74M6xO7XNt1kjjM1Y5hYTMAcrcYdpccH-AsM2ktHlXq6LQVZWrBsw02auaq2UruYfrYRcPsempJ0_0OyMe9PY9XE09lkgniPyauB6s3Ir6YjHfC7FZm5zV8WkHLFOT0cvFNSZfyT3la-1O0uYT98Fb9htv0uQM7eZHuoEf0pluF7yrR9TuKsFnCTKgRTubjdWdkx2zi3FuMjs3Gzu5dpYPgAMrv8PKpJb1paoGFR1y_-YZpUKzZuWNgqGdah_6sfSZtN6iX0yKPqM1IoDVez6MlibuTc9nQ6NxNOMgLKrTqsf6MKyJn2tU1id-PGeZOaYzgxbfcIrB0S5twntNFjFGVXatoGnoUlld0AH8dYUc3PUgSF8OFjj1mw8K2JXcTwqtFKHjSD1piA9lvbVvQmOEiopt1rnxrJQvjgt_vF6vNKEDk7I4p3k91hdxOhrGQ6wXqx_iaGPi6S3stYuD7O_h_3f6Sz3zSyJFiOCGHTL_z9u3A-m7oI92l_sVz3cp99vGh4uJBJY1R3wjQGRWHkkMJ0rhV2rteHDj-ah4loBvOmuAQvF5t1txhu-9wlaJEpVPPP0Y_RRbMC2kHpEwWuItSf9omBiJhkspqWAL5GoBbNcfLojognlQMLzuRPO7VeKwF5oAhe2PpyXJGxypVE_j8nIMZeRTi3jxRG9__iCvzUjaFTZWDepYMuyc3i6_SFZqSiUoIwCiBc-920IjCXGqNFcvfdYof4KD0DA_H0w_3DhPxdichXHFcdBF0Qt5GTugM6HhXKec_LdL_XC7m04O-N3wQf25pNN-r6jnSrS8D9Nx33s3Rsbwg8Jpm9CxYOzaPl-d6pqUwBvFYjO8WxXXHbWxVofgAQFUWkcuCEOFlk50ZXLo_NiMDMwtqgkZPsAC_3SQVlzEv-XmlloIbPXgw8rOx9D-edZEa2Pzd_nJJ1eauHJYIHUQRtd1noSh2ljjw5gYtTF9w9dUHeRUw3-mA-G7uPX37HImcU9FO3WDS7h5Butu8RT1SJ1HCnWoDYgKBNsFOI4J8SwleU_ZqbSdeb_AIt1onMTN5QOaELn8IurIJ-n0f_oT2Wg0sM0gTCAP-9o8Uot-TTjuKlcvVjrs8dH9hJSNNJ0O33DNpf_M_MKRkpgcOj_TPsS13TiVG1ADQMY.4R-szyLAhIWc5C2d-DwinA"

bot = SpeechGPT(session_token=session_token,
                wake_word="wake up",
                voice_on=True)

bot.listen()
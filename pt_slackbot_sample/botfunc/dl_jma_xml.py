import jma_weekly_weather

# 気象庁xmlデータをDLするだけのスクリプト


def main():
    jma_weekly_weather.get_jma_xml_files()


if __name__ == "__main__":
    main()

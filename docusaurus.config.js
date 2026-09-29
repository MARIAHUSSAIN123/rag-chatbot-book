// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'AI & Data Science Book',
  tagline: 'Beginner se Advanced tak | Beginner to Advanced',
  favicon: 'img/favicon.ico',
    future: {
     v4: true,
     faster: {
       swcHtmlMinimizer: false,
       swcJsMinimizer: false,
       lightningCssMinimizer: false,
     },
   },

  // Vercel deploy ke baad apna real URL yahan daalein
  url: 'https://your-book.vercel.app',
  baseUrl: '/',
  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'ur-Latn'], // ur-Latn = Roman Urdu (Latin script)
    localeConfigs: {
      en: {label: 'English', direction: 'ltr', htmlLang: 'en'},
      'ur-Latn': {label: 'Roman Urdu', direction: 'ltr', htmlLang: 'ur-Latn'},
    },
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/', // book seedha homepage par khulegi
          sidebarPath: './sidebars.js',
        },
        blog: false,
        theme: {customCss: './src/css/custom.css'},
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {respectPrefersColorScheme: true},
      navbar: {
        title: 'AI & Data Science Book',
        items: [
          {type: 'docSidebar', sidebarId: 'bookSidebar', position: 'left', label: 'Book'},
          {to: '/chatbot', label: 'Chatbot', position: 'left'},
          {type: 'localeDropdown', position: 'right'},
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Based on the SMIT AI & Data Science syllabus (Miss Javeria Hassan). Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['python', 'bash'],
      },
    }),
};

export default config;

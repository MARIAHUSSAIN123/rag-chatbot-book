// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'AI & Data Science Book',
  tagline: 'Beginner se Advanced tak | Beginner to Advanced',
  favicon: 'img/favicon.ico',
  future: {
    v4: true,
    // Windows par SWC native files ka masla aata hai, is liye ye teen band hain
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
          routeBasePath: 'docs',
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
          {type: 'localeDropdown', position: 'right'},
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Created with ♥ by Maria Hussain`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['python', 'bash'],
      },
    }),
};

export default config;
